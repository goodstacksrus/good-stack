from __future__ import annotations

import datetime
from pathlib import Path

from generator.gemini_client import GeminiClient, MockGeminiClient
from generator.image_client import fetch_article_images
from generator.markdown_writer import write_article
from generator.topic_registry import TopicRegistry


def run_pipeline(
    topic: str | None,
    output_dir: Path,
    use_mock: bool = False,
    use_grounding: bool = False,
    registry: TopicRegistry | None = None,
) -> Path | None:
    if registry is None:
        registry = TopicRegistry()

    if topic is None:
        topic = registry.next_topic()
        if topic is None:
            print("No pending topics in registry.")
            return None

    print(f"Generating article for topic: {topic}")
    llm = MockGeminiClient() if use_mock else GeminiClient()
    article = llm.generate_article(topic, use_grounding=use_grounding)
    article.front_matter.pub_date = datetime.datetime.now()

    image_keywords = article.front_matter.tags[:3] or [topic]
    images = fetch_article_images(image_keywords, count=3)

    if images:
        article.front_matter.image = images[0]
        body_images = images[1:]
        print(f"Images fetched: {len(images)} photos")
    else:
        body_images = []
        print("Images: not available (PEXELS_API_KEY not set or search failed)")

    output_path = write_article(article, output_dir, body_images=body_images)
    registry.mark_generated(topic)
    registry.add_generated_slug(article.front_matter.slug)

    print(f"Article written to: {output_path}")
    return output_path
