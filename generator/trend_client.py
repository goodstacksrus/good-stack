"""トレンドキーワード取得モジュール

A: pytrends (Google Trends) でリアルタイムトレンドを取得
B: Gemini grounding でAI生成トレンドキーワードを取得
"""
from __future__ import annotations

import json
import os
import time

from dotenv import load_dotenv

load_dotenv()

_SEED_KEYWORDS = [
    "Amazon ガジェット",
    "スマートホーム アクセサリー",
    "PC 周辺機器",
    "スマホ アクセサリー",
]

_DEFAULT_AREA = "ガジェット・家電アクセサリー"

_GEMINI_PROMPT_TEMPLATE = """\
日本のAmazonアフィリエイトサイト向けに、今トレンドの「{area}」に関する記事トピックを提案してください。

条件:
- 日本語の検索キーワードとして使えるもの
- Amazonで購入できる具体的な商品カテゴリに関連するもの
- 「おすすめ」「比較」「選び方」などの購買意向が高いキーワードを含める
- 季節・トレンドを反映した旬の話題を含める

以下のJSON配列のみを返してください（説明文なし）:
["トピック1", "トピック2", ...]

20件提案してください。
"""


def fetch_google_trends_topics(
    seed_keywords: list[str] | None = None,
    geo: str = "JP",
) -> list[str]:
    """pytrends でGoogle Trendsの関連クエリからトピックを取得する。

    Returns empty list on failure (unofficial API, may be rate-limited).
    """
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("  [trend] pytrends未インストール: pip install pytrends")
        return []

    seeds = seed_keywords or _SEED_KEYWORDS
    pytrends = TrendReq(hl="ja-JP", tz=540, timeout=(10, 25))
    results: list[str] = []

    for keyword in seeds[:4]:
        try:
            pytrends.build_payload([keyword], geo=geo, timeframe="today 3-m")
            related = pytrends.related_queries()
            top_df = related.get(keyword, {}).get("top")
            if top_df is not None and not top_df.empty:
                for query in top_df["query"].tolist()[:6]:
                    if query not in results:
                        results.append(query)
            time.sleep(1.5)
        except Exception as exc:
            print(f"  [trend/google] '{keyword}' スキップ: {exc}")

    return results


def fetch_gemini_trend_topics(area: str | None = None) -> list[str]:
    """Gemini + Google Search Grounding でトレンドトピックを生成する。"""
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if not api_key:
        print("  [trend] GOOGLE_API_KEY未設定")
        return []

    try:
        from google import genai
        from google.genai import types as genai_types
    except ImportError:
        print("  [trend] google-genai未インストール")
        return []

    model = os.getenv("LLM_MODEL", "gemini-2.5-flash")
    prompt = _GEMINI_PROMPT_TEMPLATE.format(area=area or _DEFAULT_AREA)

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=genai_types.GenerateContentConfig(
                tools=[genai_types.Tool(google_search=genai_types.GoogleSearch())],
            ),
        )
        text = response.text.strip()
        # JSON配列を抽出
        start = text.find("[")
        end = text.rfind("]") + 1
        if start >= 0 and end > start:
            topics: list[str] = json.loads(text[start:end])
            return [t for t in topics if isinstance(t, str) and t.strip()]
    except Exception as exc:
        print(f"  [trend/gemini] 失敗: {exc}")

    return []


def fetch_all_trend_topics(
    use_google: bool = True,
    use_gemini: bool = True,
    geo: str = "JP",
    seed_keywords: list[str] | None = None,
) -> list[str]:
    """AとBの両方からトピックを取得し、重複を除いて結合する。

    seed_keywords: 指定するとGoogle Trends・Gemini両方をそのジャンルに絞り込む。
    """
    results: list[str] = []
    area = "、".join(seed_keywords) if seed_keywords else None

    if use_google:
        label = f"「{area}」周辺" if area else "デフォルト"
        print(f"  [A] Google Trendsからキーワードを取得中（{label}）...")
        google_topics = fetch_google_trends_topics(seed_keywords=seed_keywords, geo=geo)
        print(f"     → {len(google_topics)}件取得")
        results.extend(google_topics)

    if use_gemini:
        label = f"「{area}」周辺" if area else "デフォルト"
        print(f"  [B] Gemini groundingでトレンドキーワードを生成中（{label}）...")
        gemini_topics = fetch_gemini_trend_topics(area=area)
        print(f"     → {len(gemini_topics)}件取得")
        for t in gemini_topics:
            if t not in results:
                results.append(t)

    return results
