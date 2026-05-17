from __future__ import annotations

import os

import httpx

_PEXELS_SEARCH = "https://api.pexels.com/v1/search"


def fetch_article_images(keywords: list[str], count: int = 3) -> list[str]:
    """Search Pexels for multiple landscape photos matching the keywords.

    Returns a list of image URLs (large size). Empty list if unavailable.
    """
    api_key = os.getenv("PEXELS_API_KEY", "")
    if not api_key:
        return []

    query = " ".join(keywords[:4])
    try:
        resp = httpx.get(
            _PEXELS_SEARCH,
            params={"query": query, "per_page": count, "orientation": "landscape"},
            headers={"Authorization": api_key},
            timeout=10.0,
        )
        resp.raise_for_status()
        photos = resp.json().get("photos", [])
        return [p["src"]["large"] for p in photos[:count]]
    except Exception as e:
        print(f"[image_client] Pexels search failed: {e}")
    return []


def fetch_article_image(keywords: list[str]) -> str:
    """Convenience wrapper — returns a single image URL or empty string."""
    results = fetch_article_images(keywords, count=1)
    return results[0] if results else ""
