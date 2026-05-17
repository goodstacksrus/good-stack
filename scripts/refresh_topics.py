"""トレンドベースのトピック補充スクリプト

使い方:
    python scripts/refresh_topics.py                          # Google Trends + Gemini（両方）
    python scripts/refresh_topics.py --source gemini          # Geminiのみ
    python scripts/refresh_topics.py --source google          # Google Trendsのみ
    python scripts/refresh_topics.py --dry-run                # 追加せず結果だけ確認
    python scripts/refresh_topics.py --add "iPhone 16 ケース" "iPad Pro スタンド"
    python scripts/refresh_topics.py --seeds "キャンプ ガジェット" "登山 アクセサリー"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from generator.topic_registry import TopicRegistry
from generator.trend_client import fetch_all_trend_topics


def main() -> None:
    parser = argparse.ArgumentParser(
        description="トピックを補充する（トレンド取得 または 直接追加）"
    )
    parser.add_argument(
        "--source",
        choices=["google", "gemini", "both"],
        default="both",
        help="取得元: google=Google Trends, gemini=Gemini grounding, both=両方（デフォルト）",
    )
    parser.add_argument(
        "--add",
        nargs="+",
        metavar="TOPIC",
        help='トピックを直接追加する（例: --add "iPhone 16 ケース" "iPad スタンド"）',
    )
    parser.add_argument(
        "--seeds",
        nargs="+",
        metavar="KEYWORD",
        help='Google Trendsの検索シードを指定（例: --seeds "キャンプ ガジェット" "登山"）',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="レジストリに追加せず、取得・指定結果だけ表示する",
    )
    parser.add_argument(
        "--min-pending",
        type=int,
        default=0,
        help="pending件数がこの値以上なら補充をスキップ（0=常に実行）。--addと併用時はスキップしない",
    )
    args = parser.parse_args()

    registry = TopicRegistry()
    current_pending = registry.pending_count()
    print(f"現在のpendingトピック数: {current_pending}件")

    # --add モード: トレンド取得をスキップして直接追加
    if args.add:
        topics = [t.strip() for t in args.add if t.strip()]
        print(f"\n直接指定トピック: {len(topics)}件")
        for i, t in enumerate(topics, 1):
            print(f"  {i:2d}. {t}")

        if args.dry_run:
            print("\n[dry-run] レジストリへの追加はスキップしました。")
            return

        added = 0
        for topic in topics:
            before = registry.pending_count()
            registry.add_topic(topic)
            if registry.pending_count() > before:
                added += 1
            else:
                print(f"  スキップ（重複）: {topic}")

        print(f"\n✓ {added}件を pending に追加しました")
        print(f"  合計pending: {registry.pending_count()}件")
        return

    # トレンド取得モード
    if args.min_pending > 0 and current_pending >= args.min_pending:
        print(f"  → {args.min_pending}件以上あるためスキップ")
        return

    use_google = args.source in ("google", "both")
    use_gemini = args.source in ("gemini", "both")

    topics = fetch_all_trend_topics(
        use_google=use_google,
        use_gemini=use_gemini,
        seed_keywords=args.seeds,
    )

    if not topics:
        print("トピックを取得できませんでした。")
        return

    print(f"\n取得したトピック候補: {len(topics)}件")
    for i, t in enumerate(topics, 1):
        print(f"  {i:2d}. {t}")

    if args.dry_run:
        print("\n[dry-run] レジストリへの追加はスキップしました。")
        return

    added = 0
    for topic in topics:
        before = registry.pending_count()
        registry.add_topic(topic)
        if registry.pending_count() > before:
            added += 1

    print(f"\n✓ {added}件を pending に追加しました（重複・生成済み除く）")
    print(f"  合計pending: {registry.pending_count()}件")


if __name__ == "__main__":
    main()
