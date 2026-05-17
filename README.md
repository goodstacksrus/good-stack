# GOOD STACK — AIアフィリエイトサイト

Amazonアソシエイト審査用の公開Webサイト。Gemini APIで記事を自動生成し、Hugo + GitHub Pagesで無料公開します。  
デザインはGear Patrol風のエディトリアルマガジンスタイル。記事ごとにPexels APIで自動取得した写真を掲載します。  
ヘッダーには段違い赤バーのSVGロゴ「GOOD STACK」を表示。

---

## このサイトの仕組み

**一言で言うと：「AIが記事を自動で書いて、写真を付けて、自動でWebに公開するサイト」**

### 登場人物（使っているサービス）

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
   「Echo Dotのケースについて書いて」
         ↓
② Pexels API で関連写真を自動取得（ヒーロー1枚＋本文2枚）
         ↓
③ Markdownファイル（YYYYMMDDHH-slug.md）が生成される
         ↓
④ Hugo が HTML に変換する
   ブラウザで表示できる Webページに整形
         ↓
⑤ GitHub Pages で世界に公開される
```

### GitHub Actions（自動化ロボット）

このプロジェクトには2つの自動ロボットが設定されています。

**ロボット① generate_articles.yml — 月・水・金 朝9時に動く**
```
朝9時になる → Python実行 → Gemini APIに記事生成依頼
→ Pexels APIで写真取得 → .mdファイルを保存 → ロボット②を呼ぶ
```

**ロボット② deploy.yml — コードが更新されたら動く**
```
新しい記事が追加される → Hugo でHTML変換
→ GitHub Pages にアップロード → サイト更新完了
```

セットアップが完了すれば、**何もしなくても週3回自動で記事が増えてサイトが更新されます。**

### Amazonアソシエイトの収益の仕組み

```
読者が記事を読む（例：「Echo Dotのケースおすすめ5選」）
  ↓
「Amazonで検索する」ボタンを押す（日本語タイトルで検索）
  ↓
Amazonで商品を購入する
  ↓
購入額の数%があなたへのキャッシュバックとして入る 💰
```

申請には審査があるため、まず記事20本以上を公開してサイトとして成立させることが先決です（Phase 1〜2の目標）。

### ファイルの役割

```
generator/   ← 「記事を書く・写真を取得する」担当（Python）
site/        ← 「見た目」担当（Hugo テンプレート・CSS）
.github/     ← 「自動化」担当（GitHub Actions）
```

---

## 構成

| レイヤー | 技術 |
|---|---|
| 記事生成 | Python + Gemini 2.5 Flash |
| 記事画像 | Pexels API（自動取得・完全無料） |
| サイト生成 | Hugo (静的サイトジェネレーター) |
| ホスティング | GitHub Pages (無料) |
| CI/CD | GitHub Actions |
| アクセス解析 | Google Analytics 4 (無料) |

---

## セットアップ

### 1. Hugo のインストール（初回のみ）

```powershell
# Scoop 経由（推奨）
scoop install hugo-extended
```

### 2. Python 環境

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 環境変数の設定

```powershell
copy .env.example .env
# .env を開いて以下を設定：
# GOOGLE_API_KEY=...  → https://aistudio.google.com/app/apikey
# PEXELS_API_KEY=...  → https://www.pexels.com/api/（無料）
```

### 4. GitHub リポジトリの設定

1. GitHubで新しいパブリックリポジトリを作成（例: `amazon-affiliate-site`）
2. Settings → Pages → Source: **GitHub Actions** を選択
3. Settings → Secrets に以下を登録:
   - `GOOGLE_API_KEY`（Gemini API）
   - `PEXELS_API_KEY`（Pexels API）
4. `site/config/_default/hugo.toml` の `baseURL` を実際のURLに変更
5. `site/static/robots.txt` の `Sitemap` URLを更新

---

## ローカル開発

```powershell
# ターミナル1: Hugo 開発サーバー（ホットリロード）
cd site
hugo server --buildDrafts --navigateToChanged
# → http://localhost:1313/amazon-affiliate-site/ で確認

# ターミナル2: 記事生成
.venv\Scripts\activate
python scripts\local_generate.py --mock                          # APIなし・確認用
python scripts\local_generate.py --topic "Echo Dot ケース"       # Gemini + 画像付き
python scripts\local_generate.py --topic "スマートプラグ" --search # Google検索 + 画像付き
```

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
  → Hugo ビルド (site/public/)
  → GitHub Pages へデプロイ
```

---

## 記事自動生成スケジュール

GitHub Actions の `generate_articles.yml` が **月・水・金の午前9時JST** に自動実行されます。

手動実行する場合は、GitHub の Actions タブ → "Generate Articles" → "Run workflow" から実行できます。

---

## フェーズ計画

| フェーズ | 目標 | 期間 |
|---|---|---|
| **Phase 1** | サイト公開（About/Privacy/Contact含む） | 1〜2週目 |
| **Phase 2** | 記事20本以上を公開、Google検索インデックス | 3〜8週目 |
| **Phase 3** | Amazonアソシエイト申請・承認後にASIN追加 | 9週目以降 |

---

## Amazonアソシエイト申請チェックリスト

- [ ] `hugo.toml` の `baseURL` を実際のGitHub PagesのURLに設定した
- [ ] About・Privacy・Contact ページが正常に表示される
- [ ] フッターにアフィリエイト開示文が表示されている
- [ ] 20本以上の記事が公開されている
- [ ] Google Analytics でアクセスが記録されている
- [ ] モバイル表示が正常（スマートフォンで確認）
- [ ] Amazonアソシエイト申請ページ: https://affiliate.amazon.co.jp/

---

## ディレクトリ構成

```
amazon_affiliate_site/
├── .github/workflows/
│   ├── deploy.yml             # push → GitHub Pages 自動デプロイ
│   ├── generate_articles.yml  # 月水金9時JST 自動記事生成
│   └── refresh_topics.yml     # 日曜9時JST 自動トピック補充
├── generator/
│   ├── models.py              # Pydanticデータモデル（image・datetime対応）
│   ├── gemini_client.py       # Gemini API / Mockクライアント（--search対応）
│   ├── image_client.py        # Pexels APIで記事画像を自動取得
│   ├── article_pipeline.py    # 生成パイプライン（記事＋画像＋日時）
│   ├── markdown_writer.py     # Hugo対応Markdown出力（本文内画像・日時ファイル名）
│   ├── topic_registry.py      # トピック管理（50件シード済み）
│   └── trend_client.py        # Google Trends + Gemini groundingでトピック取得
├── scripts/
│   ├── local_generate.py      # ローカル記事生成CLI（メイン）
│   ├── refresh_topics.py      # トピック補充CLI（--add / --seeds / --source）
│   ├── list_models.py         # 利用可能なモデル一覧表示
│   └── test_api.py            # APIキー動作確認用
├── site/
│   ├── config/_default/
│   │   ├── hugo.toml          # baseURL を変更する ⚠️
│   │   ├── params.toml        # ga4_id を入力する
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
