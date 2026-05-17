"""ローカル記事生成CLI

Usage:
    python scripts/local_generate.py --mock
    python scripts/local_generate.py --topic "Echo Dot ケース おすすめ" --mock
    python scripts/local_generate.py --topic "スマートプラグ おすすめ"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# プロジェクトルートをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

from generator.article_pipeline import run_pipeline
from generator.topic_registry import TopicRegistry


def main() -> None:
    parser = argparse.ArgumentParser(description="記事生成CLI")
    parser.add_argument("--topic", default="", help="記事のトピック（省略するとレジストリから自動選択）")
    parser.add_argument(
        "--output-dir",
        default="site/content/articles/",
        help="出力ディレクトリ（デフォルト: site/content/articles/）",
    )
    parser.add_argument("--mock", action="store_true", help="モッククライアントを使用（APIキー不要）")
    parser.add_argument("--search", action="store_true", help="Google検索で最新情報を取得してから記事生成（Grounding有効）")
    args = parser.parse_args()

    topic = args.topic.strip() or None
    output_dir = Path(args.output_dir)
    registry = TopicRegistry()

    if topic is None and registry.pending_count() == 0:
        print("全トピックの記事生成が完了しています。--topic で新しいトピックを指定してください。")
        sys.exit(0)

    result = run_pipeline(
        topic=topic,
        output_dir=output_dir,
        use_mock=args.mock,
        use_grounding=args.search,
        registry=registry,
    )

    if result:
        print(f"完了: {result}")
        print(f"残りトピック数: {registry.pending_count()}")
    else:
        print("記事の生成に失敗しました。")
        sys.exit(1)


if __name__ == "__main__":
    main()
