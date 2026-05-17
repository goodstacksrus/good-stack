from __future__ import annotations

import json
from pathlib import Path

_SEED_TOPICS = [
    # スマートスピーカー
    "Echo Dot 第5世代 ケース",
    "Echo Show 8 スタンド",
    "Echo Pop カバー",
    "Amazon Echo 壁掛けホルダー",
    "Google Nest Mini スタンド",
    # スマートプラグ・スマートホーム
    "スマートプラグ おすすめ 節電",
    "スマートリモコン 赤外線 おすすめ",
    "スマートホーム ハブ 比較",
    "スマート電球 E26 おすすめ",
    "スマートカーテン レール 後付け",
    # Fire TV / Chromecast
    "Fire TV Stick リモコン 電池 交換",
    "Fire TV Stick ケーブル 延長",
    "Chromecast with Google TV ケース",
    "Fire TV Stick 4K MAX 壁掛け",
    # キッチン家電アクセサリー
    "エアフライヤー シリコンライナー おすすめ",
    "エアフライヤー アクセサリーセット 比較",
    "電気ケトル 保温カバー おすすめ",
    "コーヒーメーカー フィルター 互換品",
    "電動ミル アクセサリー おすすめ",
    "ヨーグルトメーカー 容器 追加",
    # PC周辺機器
    "ノートPC スタンド 折りたたみ おすすめ",
    "ノートPC 冷却パッド 静音 おすすめ",
    "ワイヤレスキーボード コンパクト 比較",
    "マウスパッド 大型 おすすめ",
    "USB-Cハブ 7ポート おすすめ",
    "モニターアーム シングル おすすめ",
    "ウェブカメラ スタンド 卓上",
    "ヘッドセット スタンド 木製",
    # スマートフォンアクセサリー
    "ワイヤレス充電器 スタンド型 おすすめ",
    "スマホスタンド 卓上 角度調整",
    "MagSafe 対応 ウォレット おすすめ",
    "iPhone 15 ケース クリア 耐衝撃",
    "Android スマホ 防水ケース おすすめ",
    "スマホ リングホルダー おすすめ",
    # タブレットアクセサリー
    "iPad スタンド 折りたたみ おすすめ",
    "Fire HD 10 ケース キーボード付き",
    "タブレット スタイラスペン 互換品",
    "iPad mini 保護フィルム 比較",
    # ゲーム周辺機器
    "Nintendo Switch ケース おすすめ",
    "Switch コントローラー グリップ",
    "PS5 コントローラー 充電スタンド",
    "ゲーミングヘッドセット スタンド おすすめ",
    # 収納・整理
    "ケーブル 収納 マグネット おすすめ",
    "充電ステーション 複数 USB おすすめ",
    "デスク 小物収納 おすすめ",
    "電源タップ USB付き 縦型",
    # カメラ・ビデオ
    "ウェブカメラ ライトリング セット",
    "スマホ 三脚 コンパクト おすすめ",
    "アクションカメラ マウント おすすめ",
    "カメラ バッテリー 互換品 比較",
]

_DEFAULT_REGISTRY_PATH = Path(__file__).parent.parent / "topic_registry.json"


class TopicRegistry:
    def __init__(self, registry_path: Path = _DEFAULT_REGISTRY_PATH) -> None:
        self._path = registry_path
        self._data = self._load()

    def _load(self) -> dict:
        if self._path.exists():
            return json.loads(self._path.read_text(encoding="utf-8"))
        return {"generated": [], "pending": list(_SEED_TOPICS)}

    def _save(self) -> None:
        self._path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def next_topic(self) -> str | None:
        pending = self._data.get("pending", [])
        return pending[0] if pending else None

    def mark_generated(self, topic: str) -> None:
        self._data["pending"] = [t for t in self._data.get("pending", []) if t != topic]
        if topic not in self._data.get("generated", []):
            self._data.setdefault("generated", []).append(topic)
        self._save()

    def add_topic(self, topic: str) -> None:
        if topic not in self._data.get("pending", []) and topic not in self._data.get("generated", []):
            self._data.setdefault("pending", []).append(topic)
            self._save()

    def pending_count(self) -> int:
        return len(self._data.get("pending", []))

    def generated_slugs(self) -> list[str]:
        return self._data.get("generated_slugs", [])

    def add_generated_slug(self, slug: str) -> None:
        self._data.setdefault("generated_slugs", [])
        if slug not in self._data["generated_slugs"]:
            self._data["generated_slugs"].append(slug)
        self._save()
