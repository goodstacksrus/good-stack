import pytest
from pathlib import Path

from generator.article_pipeline import run_pipeline
from generator.topic_registry import TopicRegistry


def test_run_pipeline_mock(tmp_path: Path):
    registry = TopicRegistry(registry_path=tmp_path / "registry.json")
    output_path = run_pipeline(
        topic="Echo Dot ケース おすすめ",
        output_dir=tmp_path / "articles",
        use_mock=True,
        registry=registry,
    )
    assert output_path is not None
    assert output_path.exists()
    content = output_path.read_text(encoding="utf-8")
    assert "---" in content
    assert "## " in content


def test_run_pipeline_auto_topic(tmp_path: Path):
    registry = TopicRegistry(registry_path=tmp_path / "registry.json")
    first_topic = registry.next_topic()
    assert first_topic is not None

    output_path = run_pipeline(
        topic=None,  # レジストリから自動選択
        output_dir=tmp_path / "articles",
        use_mock=True,
        registry=registry,
    )
    assert output_path is not None
    # 生成済みに移動されていること
    assert first_topic in registry._data["generated"]


def test_run_pipeline_empty_registry(tmp_path: Path):
    registry = TopicRegistry(registry_path=tmp_path / "registry.json")
    registry._data = {"generated": [], "pending": []}
    registry._save()

    result = run_pipeline(
        topic=None,
        output_dir=tmp_path / "articles",
        use_mock=True,
        registry=registry,
    )
    assert result is None
