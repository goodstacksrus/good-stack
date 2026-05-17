import datetime
import pytest
from pydantic import ValidationError

from generator.models import Article, ArticleFrontMatter, ArticleSection


def _make_front_matter(**kwargs) -> ArticleFrontMatter:
    defaults = dict(
        title="テスト記事タイトル",
        slug="test-article",
        pub_date=datetime.date.today(),
        description="これはテスト用のメタディスクリプションです。テスト目的で使用するためのダミーの説明文で、最低文字数を超える十分な長さがあります。",
        tags=["テスト", "アクセサリー"],
        categories=["スマートホーム"],
    )
    defaults.update(kwargs)
    return ArticleFrontMatter(**defaults)


def _make_section(**kwargs) -> ArticleSection:
    defaults = dict(heading="セクション見出し", content="これはセクションの本文です。テスト目的で使用するコンテンツで、最低文字数を超えるよう十分な長さに書いています。")
    defaults.update(kwargs)
    return ArticleSection(**defaults)


def test_front_matter_valid():
    fm = _make_front_matter()
    assert fm.slug == "test-article"
    assert fm.draft is False


def test_front_matter_description_too_short():
    with pytest.raises(ValidationError):
        _make_front_matter(description="短すぎる")


def test_section_content_too_short():
    with pytest.raises(ValidationError):
        _make_section(content="短")


def test_article_valid():
    fm = _make_front_matter()
    sections = [_make_section() for _ in range(3)]
    article = Article(
        front_matter=fm,
        intro="導入文です。" * 10,
        sections=sections,
        buying_guide="購入ガイドの本文です。" * 15,
        conclusion="まとめの文章です。" * 8,
    )
    assert article.affiliate_placeholder == "AMAZON_LINK_PLACEHOLDER_test-article"


def test_article_requires_min_sections():
    fm = _make_front_matter()
    with pytest.raises(ValidationError):
        Article(
            front_matter=fm,
            intro="導入文です。" * 10,
            sections=[_make_section(), _make_section()],  # 2つ（最低3つ必要）
            buying_guide="購入ガイドです。" * 15,
            conclusion="まとめです。" * 8,
        )
