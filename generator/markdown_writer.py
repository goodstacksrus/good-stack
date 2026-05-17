from __future__ import annotations

from pathlib import Path

import yaml

from generator.models import Article

# Insert body images after these section indices (0-based)
_IMAGE_AFTER = {0, 2}


def write_article(
    article: Article,
    output_dir: Path,
    body_images: list[str] | None = None,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    fm = article.front_matter
    body_images = body_images or []

    front_matter = {
        "title": fm.title,
        "slug": fm.slug,
        "date": fm.pub_date.strftime("%Y-%m-%dT%H:%M:%S"),
        "description": fm.description,
        "tags": fm.tags,
        "categories": fm.categories,
        "draft": fm.draft,
    }
    if fm.image:
        front_matter["image"] = fm.image

    lines = ["---"]
    lines.append(yaml.dump(front_matter, allow_unicode=True, default_flow_style=False).rstrip())
    lines.append("---")
    lines.append("")
    lines.append(article.intro)
    lines.append("")

    img_idx = 0
    for i, section in enumerate(article.sections):
        lines.append(f"## {section.heading}")
        lines.append("")
        lines.append(section.content)
        lines.append("")
        if img_idx < len(body_images) and i in _IMAGE_AFTER:
            lines.append(f"![{section.heading}]({body_images[img_idx]})")
            lines.append("")
            img_idx += 1

    lines.append("## 選び方のポイント")
    lines.append("")
    lines.append(article.buying_guide)
    lines.append("")
    lines.append(f'{{{{< affiliate-button slug="{fm.slug}" keyword="{fm.title}" >}}}}')
    lines.append("")
    lines.append("## まとめ")
    lines.append("")
    lines.append(article.conclusion)
    lines.append("")

    content = "\n".join(lines)
    timestamp = fm.pub_date.strftime("%Y%m%d%H")
    output_path = output_dir / f"{timestamp}-{fm.slug}.md"
    output_path.write_text(content, encoding="utf-8")
    return output_path
