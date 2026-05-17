# GOOD STACK — AIキュレーションメディア

モノ選び・お金の知識・最新時事をキュレーションして届けるメディア。  
Gemini APIで記事を自動生成し、Hugo + GitHub Pages で公開しています。  
デザインはGear Patrol風のエディトリアルマガジンスタイル。

- **サイト**: https://goodstacksrus.github.io/good-stack/
- **リポジトリ**: https://github.com/goodstacksrus/good-stack

---

## このサイトの仕組み

**一言で言うと：「AIが記事を自動で書いて、写真を付けて、自動でWebに公開するサイト」**

### 使っているサービス

| 名前 | 役割 | 料金 |
|---|---|---|
| **Python + Gemini API** | 記事の文章を書くAI | 無料枠あり |
| **Pexels API** | 記事に合う写真を自動取得 | 完全無料 |
| **Hugo** | Markdownを綺麗なHTMLページに変換するツール | 無料 |
| **GitHub** | コードの保管・自動作業・サイト公開をまとめて担う | 無料 |
| **Google Analytics** | 誰が見に来たかを計測 | 無料 |

### 記事が公開されるまでの流れ

```
① Python が Gemini AI に記事執筆を依頼
         ↓
② Pexels API で関連写真を自動取得（ヒーロー1枚＋本文2枚）
         ↓
③ Markdownファイル（YYYYMMDDHH-slug.md）が生成される
         ↓
④ Hugo が HTML に変換する
         ↓
⑤ GitHub Pages で世界に公開される
```

### GitHub Actions（自動化）

**generate_articles.yml — 月・水・金 朝9時JST**
```
朝9時になる → Gemini APIに記事生成依頼 → Pexels APIで写真取得
→ .mdファイルを保存 → deploy.yml を呼ぶ
```

**refresh_topics.yml — 毎週日曜 朝9時JST**
```
Google Trends + Gemini Grounding でトレンドトピックを取得
→ topic_registry.json に追加
```

**deploy.yml — コードが更新されたら自動実行**
```
新しい記事が追加される → Hugo でHTML変換 → GitHub Pages にアップロード
```

セットアップが完了すれば、**何もしなくても週3回自動で記事が増えてサイトが更新されます。**

---

## 構成

| レイヤー | 技術 |
|---|---|
| 記事生成 | Python + Gemini 2.5 Flash |
| 記事画像 | Pexels API（自動取得・完全無料） |
| サイト生成 | Hugo (静的サイトジェネレーター) |
| ホスティング | GitHub Pages (無料) |
| CI/CD | GitHub Actions |
| アクセス解析 | Google Analytics 4 (未設定) |

---

## ローカル開発

```powershell
# 1. 仮想環境を有効化
cd C:\Users\oueno\venv\good-stack
.venv\Scripts\activate

# 2. ターミナルを別に開いて Hugo 開発サーバーを起動
cd site
hugo server --buildDrafts --buildFuture --navigateToChanged
# → http://localhost:1313/good-stack/ で確認

# 3. 記事を生成
python scripts\local_generate.py --mock                    # APIなし・確認用
python scripts\local_generate.py --topic "テーマ"          # Gemini + 画像付き
python scripts\local_generate.py --topic "テーマ" --search # Google検索 + 画像付き
```

詳細は [USAGE.md](USAGE.md) を参照。

---

## テスト

```powershell
pytest tests/ -v
```

---

## デプロイフロー

```
main ブランチへのpush
  → deploy.yml が起動
  → Hugo ビルド (--buildFuture)
  → GitHub Pages へデプロイ（約1〜2分）
```

---

## フェーズ計画

| フェーズ | 目標 | 状態 |
|---|---|---|
| **Phase 1** | サイト公開・GA4設定・Search Console登録 | 進行中 |
| **Phase 2** | 記事20本以上・Google検索インデックス | 未着手 |
| **Phase 3** | Amazonアソシエイト申請・ASIN登録・収益化 | 未着手 |

---

## Amazonアソシエイト申請チェックリスト（Phase 3で使う）

- [x] `hugo.toml` の `baseURL` を実際のGitHub PagesのURLに設定した
- [x] About・Privacy・Contact ページが正常に表示される
- [x] フッターにアフィリエイト開示文が表示されている
- [ ] 20本以上の記事が公開されている
- [ ] Google Analytics でアクセスが記録されている
- [x] モバイル表示が正常（ハンバーガーメニュー対応済み）
- [ ] 申請: https://affiliate.amazon.co.jp/

---

## ディレクトリ構成

```
good-stack/
├── .github/workflows/
│   ├── deploy.yml             # push → GitHub Pages 自動デプロイ
│   ├── generate_articles.yml  # 月水金9時JST 自動記事生成
│   └── refresh_topics.yml     # 日曜9時JST 自動トピック補充
├── generator/
│   ├── models.py              # Pydanticデータモデル
│   ├── gemini_client.py       # Gemini API（--search対応）
│   ├── image_client.py        # Pexels APIで記事画像を自動取得
│   ├── article_pipeline.py    # 生成パイプライン
│   ├── markdown_writer.py     # Hugo対応Markdown出力
│   ├── topic_registry.py      # トピック管理
│   └── trend_client.py        # Google Trends + Gemini groundingでトピック取得
├── scripts/
│   ├── local_generate.py      # ローカル記事生成CLI（メイン）
│   ├── refresh_topics.py      # トピック補充CLI
│   ├── list_models.py         # 利用可能なモデル一覧表示
│   └── test_api.py            # APIキー動作確認用
├── site/
│   ├── config/_default/
│   │   ├── hugo.toml          # baseURL設定済み
│   │   ├── params.toml        # ga4_id を入力する ⚠️
│   │   └── menus.toml         # ナビゲーション設定
│   ├── content/
│   │   ├── about.md           # Amazon審査必須
│   │   ├── privacy.md         # Amazon審査必須
│   │   ├── contact.md         # Amazon審査必須
│   │   └── articles/          # 生成記事（YYYYMMDDHH-slug.md）
│   ├── layouts/               # HTMLテンプレート
│   └── static/
│       ├── css/main.css       # メインCSS（Gear Patrol風デザイン）
│       └── robots.txt
├── tests/                     # pytestテスト
├── topic_registry.json        # トピック管理DB（pending / generated）
├── .env                       # APIキー設定（gitignore済み・要秘匿）
├── .env.example               # .env のテンプレート
└── requirements.txt
```
