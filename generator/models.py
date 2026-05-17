import datetime
from typing import List

from pydantic import BaseModel, Field


class ArticleSection(BaseModel):
    heading: str = Field(..., description="H2 section heading")
    content: str = Field(..., min_length=50, description="Section body text (150-300 words)")


class ArticleFrontMatter(BaseModel):
    title: str = Field(..., description="Article title for <h1> and <title>")
    slug: str = Field(..., description="URL-safe filename slug")
    pub_date: datetime.datetime = Field(default_factory=datetime.datetime.now)
    description: str = Field(..., min_length=50, max_length=160)
    tags: List[str] = Field(default_factory=list)
    categories: List[str] = Field(default_factory=list)
    draft: bool = False
    image: str = ""


class Article(BaseModel):
    front_matter: ArticleFrontMatter
    intro: str = Field(..., min_length=30, description="Opening hook paragraph")
    sections: List[ArticleSection] = Field(..., min_length=3)
    buying_guide: str = Field(..., min_length=50, description="'How to choose' section")
    conclusion: str = Field(..., min_length=30)

    @property
    def affiliate_placeholder(self) -> str:
        return f"AMAZON_LINK_PLACEHOLDER_{self.front_matter.slug}"
