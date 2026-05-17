from pathlib import Path
from datetime import date

from generator.gemini_client import MockGeminiClient
from generator.markdown_writer import write_article


def test_write_article_creates_file(tmp_path: Path):
    client = MockGeminiClient()
    article = client.generate_article("スマートプラグ おすすめ")
    output_path = write_article(article, tmp_path)

    assert output_path.exists()
    assert output_path.suffix == ".md"


def test_write_article_has_frontmatter(tmp_path: Path):
    client = MockGeminiClient()
    article = client.generate_article("Echo Dot ケース")
    output_path = write_article(article, tmp_path)

    content = output_path.read_text(encoding="utf-8")
    assert content.startswith("---")
    assert "title:" in content
    assert "slug:" in content
    assert "date:" in content
    assert "description:" in content


def test_write_article_has_sections(tmp_path: Path):
    client = MockGeminiClient()
    article = client.generate_article("スマートリモコン 比較")
    output_path = write_article(article, tmp_path)

    content = output_path.read_text(encoding="utf-8")
    assert "## " in content
    assert "affiliate-button" in content
    assert "選び方のポイント" in content
    assert "まとめ" in content
