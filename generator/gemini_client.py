import datetime
import json
import os
import re

from dotenv import load_dotenv
from google import genai
from google.genai import types as genai_types

from generator.models import Article, ArticleFrontMatter, ArticleSection

load_dotenv()

_SYSTEM_INSTRUCTION = """
あなたは日本語のアマゾンアソシエイト向けレビューライターです。
与えられたトピックについて、読者に役立つ詳細な製品アクセサリー紹介記事を書いてください。
- 正確で実用的な情報を提供する
- 購買意欲を高めるが、誇張しない
- 自然な日本語で書く
- SEOを意識したキーワードを自然に含める
"""


class GeminiClient:
    def __init__(self) -> None:
        self._client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
        self._model = os.getenv("LLM_MODEL", "gemini-2.5-flash")

    def generate_article(self, topic: str, use_grounding: bool = False) -> Article:
        research = self._research_topic(topic) if use_grounding else None
        if research:
            print("  検索完了。記事を生成中...")

        outline = self._generate_outline(topic, research)
        sections = self._generate_sections(topic, outline["section_headings"], research)

        front_matter = ArticleFrontMatter(
            title=outline["title"],
            slug=outline["slug"],
            pub_date=datetime.date.today(),
            description=outline["description"],
            tags=outline["tags"],
            categories=outline["categories"],
        )
        return Article(
            front_matter=front_matter,
            intro=outline["intro"],
            sections=sections,
            buying_guide=outline["buying_guide"],
            conclusion=outline["conclusion"],
        )

    def _research_topic(self, topic: str) -> str:
        """Google検索でトピックの最新情報を収集する"""
        print("  Google検索中...")
        prompt = (
            f"「{topic}」について以下の情報を調査してください:\n"
            f"- Amazonで人気の具体的な製品名と価格帯\n"
            f"- 各製品の主な特徴・スペック\n"
            f"- ユーザーレビューで評価されている点・不満な点\n"
            f"- 選び方のポイント\n"
            f"日本語で詳しくまとめてください。"
        )
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=genai_types.GenerateContentConfig(
                tools=[genai_types.Tool(google_search=genai_types.GoogleSearch())],
            ),
        )
        return response.text

    def _generate_outline(self, topic: str, research: str | None = None) -> dict:
        schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "slug": {"type": "string"},
                "description": {"type": "string"},
                "tags": {"type": "array", "items": {"type": "string"}},
                "categories": {"type": "array", "items": {"type": "string"}},
                "intro": {"type": "string"},
                "section_headings": {"type": "array", "items": {"type": "string"}},
                "buying_guide": {"type": "string"},
                "conclusion": {"type": "string"},
            },
            "required": [
                "title", "slug", "description", "tags", "categories",
                "intro", "section_headings", "buying_guide", "conclusion",
            ],
        }
        context = f"\n\n【最新検索情報】\n{research}" if research else ""
        prompt = f"""
トピック: {topic}{context}

以下を含むアウトラインをJSONで返してください:
- title: 記事タイトル（H1用、SEO最適化済み）
- slug: URLスラッグ（英数字とハイフンのみ、例: "echo-dot-case-review"）
- description: メタディスクリプション（120〜160文字）
- tags: タグリスト（3〜5個）
- categories: カテゴリリスト（1〜2個）
- intro: 導入文（150字以上）
- section_headings: H2見出しのリスト（5〜7個）
- buying_guide: 購入ガイドの本文（200字以上、「選び方のポイント」セクション）
- conclusion: まとめ（150字以上）
"""
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=genai_types.GenerateContentConfig(
                system_instruction=_SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_schema=schema,
            ),
        )
        return json.loads(response.text)

    def _generate_sections(
        self, topic: str, headings: list[str], research: str | None = None
    ) -> list[ArticleSection]:
        context = f"\n\n【最新検索情報】\n{research}" if research else ""
        sections = []
        for heading in headings:
            prompt = f"""
トピック: {topic}{context}
セクション見出し: {heading}

このH2セクションの本文を200〜300字で書いてください。
具体的な製品情報、使い方、メリット・デメリットを含めてください。
テキストのみ返してください（見出し不要）。
"""
            response = self._client.models.generate_content(
                model=self._model,
                contents=prompt,
                config=genai_types.GenerateContentConfig(
                    system_instruction=_SYSTEM_INSTRUCTION,
                ),
            )
            sections.append(ArticleSection(heading=heading, content=response.text.strip()))
        return sections


class MockGeminiClient:
    """API呼び出しなしでローカルテスト用のモッククライアント"""

    def generate_article(self, topic: str, use_grounding: bool = False) -> Article:
        slug = re.sub(r"[^a-z0-9-]", "", topic.lower().replace(" ", "-").replace("　", "-"))
        slug = re.sub(r"-+", "-", slug).strip("-")[:50] or f"article-{abs(hash(topic)) % 100000}"
        front_matter = ArticleFrontMatter(
            title=f"【2026年版】{topic}おすすめ5選｜選び方も解説",
            slug=slug,
            pub_date=datetime.date.today(),
            description=f"{topic}の選び方とおすすめ製品を徹底解説。Amazonで買える人気モデルを比較して、あなたにぴったりの一品を見つけましょう。",
            tags=["アクセサリー", "おすすめ", "比較"],
            categories=["スマートホーム"],
        )
        sections = [
            ArticleSection(
                heading=f"{topic}とは？基本を解説",
                content=f"{topic}は、メイン製品をより便利・快適に使うための周辺アクセサリーです。適切なものを選ぶことで、日々の使い勝手が大きく向上します。本記事では主要モデルの特徴を詳しく比較します。",
            ),
            ArticleSection(
                heading="注目の人気モデル3選",
                content="1. スタンダードモデル：コストパフォーマンスに優れ、初めての方にもおすすめ。2. プレミアムモデル：耐久性と機能性を重視したい方向け。3. コンパクトモデル：持ち運びや省スペースを重視する方に最適です。",
            ),
            ArticleSection(
                heading="素材・耐久性の比較",
                content="シリコン素材は柔軟性があり装着しやすく、TPU素材は衝撃吸収性が高い点が特徴です。長期使用を考えると、素材の品質が重要な判断基準になります。各モデルの素材特性を詳しく比較しました。",
            ),
            ArticleSection(
                heading="価格帯と予算の考え方",
                content="エントリーモデルは500〜1,500円、ミドルレンジは1,500〜3,000円、プレミアムモデルは3,000円以上が目安です。用途と使用頻度に応じて、適切な予算帯を選ぶことが大切です。",
            ),
            ArticleSection(
                heading="ユーザーレビューから見る実際の使い心地",
                content="Amazonレビューを分析すると、高評価モデルに共通するのは「フィット感の良さ」「操作性の維持」「素材の品質」の3点です。★4以上の製品を中心に、実際の使用感をまとめました。",
            ),
        ]
        return Article(
            front_matter=front_matter,
            intro=f"{topic}をお探しですか？適切なアクセサリーを選ぶことで、メイン製品の使い勝手が格段に向上します。本記事では、Amazonで人気の{topic}をランキング形式で紹介し、選び方のポイントも詳しく解説します。",
            sections=sections,
            buying_guide=f"{topic}を選ぶ際は「対応機種の確認」「素材の品質」「レビュー数と評価」の3点を重視しましょう。特に対応機種の確認は必須です。購入前に必ず型番を確認してください。",
            conclusion=f"今回は{topic}のおすすめ製品と選び方を紹介しました。自分の用途に合ったアクセサリーを選んで、毎日の生活をより快適にしましょう。ご不明な点はコメント欄でお気軽にどうぞ。",
        )
