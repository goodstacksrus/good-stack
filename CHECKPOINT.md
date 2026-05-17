# 作業チェックポイント — GOOD STACK

最終更新: 2026-05-17

## 現在地（ここから再開）

**GitHub公開済み（goodstacksrus/good-stack）→ 次は STEP 4（GitHub Secrets登録）**

---

## 完了済み ✅

| 項目 | 詳細 |
|---|---|
| Python記事生成パッケージ | models / gemini_client / pipeline / writer / registry |
| テスト | `pytest tests/ -v` → 11テスト全パス |
| Hugoサイト | レイアウト・CSS・SEOメタタグ・GA4対応済み |
| 固定ページ | About / Privacy Policy / Contact（Amazon審査必須の3ページ） |
| GitHub Actions | deploy.yml / generate_articles.yml（月水金9時JST自動生成） |
| トピックシード | 50件 `generator/topic_registry.py` に登録済み |
| ローカル動作確認 | Hugo開発サーバー・記事生成（Gemini実API）・モック生成すべて動作済み |
| Google検索Grounding | `--search` フラグで最新情報を取得して記事生成できる |
| セキュリティレビュー | APIキー漏洩なし確認済み・GitHub Actionsのシェルインジェクション対策済み |
| 記事の並び順 | 新しい順（ByDate.Reverse）・左から最新順で表示 |
| 使い方ドキュメント | `USAGE.md` 作成済み |
| **デザイン刷新** | Gear Patrol風（黒ヘッダー・赤アクセント・Playfair Displayセリフ体・マガジングリッド） |
| **CSSパス修正** | `assets/css/` → `static/css/main.css` に移動（表示されなかった問題を解決） |
| **Pexels画像統合** | 記事生成時に自動でヒーロー画像＋本文内2枚を取得 |
| **カテゴリバー** | ヘッダー下にカテゴリナビゲーションを追加（ByCount動的表示） |
| **記事日時** | `pub_date` を `datetime.datetime`（時刻付き）に変更・ファイル名に年月日時を付与 |
| **Amazon検索キーワード** | 英語スラッグ → 日本語タイトルで検索するよう変更 |
| **サイト名変更** | 「アクセサリーラボ」→「GOOD STACK」（hugo.toml のtitle） |
| **SVGロゴ** | ヘッダーに段違い赤バー＋GOOD/STACKテキストのロゴを実装 |
| **リンク修正** | `relURL` → `.Site.Home.RelPermalink` / `.Site.GetPage` でリンク切れ解消 |
| **未来日付記事の表示** | `--buildFuture` フラグ追加（ローカル・deploy.yml両方） |
| **トレンドトピック補充** | `generator/trend_client.py`：pytrends(Google Trends) + Gemini groundingのA+Bハイブリッド |
| **補充CLI** | `scripts/refresh_topics.py`：`--add` / `--seeds` / `--source` / `--dry-run` / `--min-pending` |
| **自動補充ワークフロー** | `.github/workflows/refresh_topics.yml`：毎週日曜9時JSTに自動実行 |
| **コードレビュー P0修正** | 下記5件を一括修正（GitHub公開前の必須対応） |
| ┗ PEXELS_API_KEY漏れ | `generate_articles.yml` にenv追加（本番で画像が出ない問題を防止） |
| ┗ Trigger deploy修正 | ステップ内 `uses:` → 別ジョブ `needs: generate` + reusable workflow呼び出し |
| ┗ 残存relURL除去 | `header.html`カテゴリバー / `single.html`パンくず・タグを `.Site.GetPage` 化 |
| ┗ affiliate-button修正 | `hugo.Data` → `site.Data`（hugo.Dataは無効な構文のため） |
| ┗ テンプレ空白除去 | `{{- -}}` で `range`/`with` の空白を抑制（dev サーバーでのレイアウト崩れ防止） |
| **記事テンプレ統一** | `_default/page.html` 削除 → 全記事が `single.html`（hero画像・breadcrumb・タグ付き）で描画 |
| **section別条件分岐** | `single.html` の meta/tags は `articles` セクションのみ表示（about/privacy/contactで日付ゴミ表示なし） |
| **CSSパス修正（再）** | `head.html` を `absURL` → `relURL` に変更（dev server で本番URLを参照していた問題を解決） |
| **assets/css/ 削除** | 未使用ディレクトリを削除し編集対象を `static/css/main.css` 一箇所に統一 |
| **ホームリード文刷新** | バッジ「Daily Good Picks」・三本柱（モノ・お金・時事）に変更 |
| **モバイル対応** | ハンバーガーメニュー実装（600px以下） |
| **About/Contact更新** | 「アクセサリーラボ」→「GOOD STACK」・三本柱対応に刷新 |
| **STEP 1 完了** | baseURL → `https://goodstacksrus.github.io/good-stack/` |
| **STEP 2 完了** | goodstacksrus/good-stack（public）にpush済み |
| **STEP 3 完了** | GitHub Pages → Source: GitHub Actions 設定済み・公開中 |

---

## 次にやること（未完了）

### STEP 4 — APIキーを GitHub Secrets に登録

GitHubリポジトリ → **Settings → Secrets and variables → Actions** → `New repository secret`

| Secret名 | 値 | 用途 |
|---|---|---|
| `GOOGLE_API_KEY` | Gemini APIキー | 記事生成 |
| `PEXELS_API_KEY` | Pexels APIキー | 記事画像取得 |

### STEP 5 — Google Analytics 4 設定（推奨）

1. https://analytics.google.com → 新しいプロパティを作成
2. 測定ID（`G-XXXXXXXXXX`）を取得
3. [site/config/_default/params.toml](site/config/_default/params.toml) を編集:
   ```toml
   ga4_id = "G-XXXXXXXXXX"
   ```

### STEP 6 — Google Search Console 登録（インデックスに必要）

1. https://search.google.com/search-console → プロパティ追加
2. HTMLファイル認証 → ダウンロードしたファイルを `site/static/` に置く
3. `git push` → 認証完了
4. サイトマップ送信: `https://goodstacksrus.github.io/good-stack/sitemap.xml`

---

## 環境情報

| 項目 | 内容 |
|---|---|
| Python | 3.13.12 |
| Hugo | v0.161.1-extended |
| Scoop | v0.5.3 |
| 使用モデル | `gemini-2.5-flash`（`.env` の `LLM_MODEL` で変更可） |
| 仮想環境 | `.venv\Scripts\activate` で有効化 |
| 記事画像 | Pexels API（`.env` の `PEXELS_API_KEY` で有効化） |
| GitHub | https://github.com/goodstacksrus/good-stack |
| サイトURL | https://goodstacksrus.github.io/good-stack/ |

---

## ローカル開発の再開手順

```powershell
# 1. 仮想環境を有効化
cd C:\Users\oueno\venv\good-stack
.venv\Scripts\activate

# 2. Hugo開発サーバーを起動（別ターミナル）
cd site
hugo server --buildDrafts --buildFuture --navigateToChanged
# → http://localhost:1313/good-stack/

# 3. 記事を生成（元のターミナルに戻って）
python scripts\local_generate.py --search   # Google検索つき（高品質）・Pexels画像付き
python scripts\local_generate.py            # 通常生成・Pexels画像付き
python scripts\local_generate.py --mock     # APIなし確認用（画像なし）
```

詳細は [USAGE.md](USAGE.md) を参照。

---

## フェーズ別ゴール

```
Phase 1（今） → GitHub公開済み・GA4設定・Search Console登録
Phase 2（3〜8週目） → 記事20本自動生成・Google検索インデックス
Phase 3（9週目〜） → Amazonアソシエイト申請 → ASIN登録 → 収益化
```

### Amazonアソシエイト申請チェックリスト（Phase 3で使う）

- [ ] baseURL が実際のGitHub PagesのURLになっている
- [ ] About・Privacy・Contact ページが正常表示される
- [ ] フッターにアフィリエイト開示文が表示されている
- [ ] 記事が20本以上公開されている
- [ ] Google Analytics でアクセスが記録されている
- [ ] スマートフォンで表示確認済み
- [ ] 申請先: https://affiliate.amazon.co.jp/

---

## ファイルマップ（主要ファイルの場所）

```
good-stack/
├── CHECKPOINT.md              ← このファイル（作業状況）
├── USAGE.md                   ← 使い方ガイド（コマンド一覧）
├── README.md                  ← プロジェクト全体説明
├── .env                       ← APIキー設定（gitignore済み・要秘匿）
├── .env.example               ← .env のテンプレート（キーなし）
├── requirements.txt
├── topic_registry.json        ← トピック管理DB（pending / generated）
├── generator/
│   ├── gemini_client.py       ← GeminiClient（--search でGrounding有効）
│   ├── image_client.py        ← Pexels APIで記事画像を取得
│   ├── topic_registry.py      ← トピックのシードリスト
│   ├── trend_client.py        ← Google Trends + Gemini groundingでトピック取得
│   ├── article_pipeline.py    ← 生成パイプライン（画像取得・日時付与を含む）
│   ├── markdown_writer.py     ← Hugo対応Markdown出力（本文内画像挿入・日時ファイル名）
│   └── models.py              ← Pydanticモデル定義（image・datetime対応）
├── scripts/
│   ├── local_generate.py      ← 記事生成CLI（メイン）
│   ├── refresh_topics.py      ← トピック補充CLI（--add / --seeds / --source）
│   ├── list_models.py         ← 利用可能なモデル一覧表示
│   └── test_api.py            ← APIキー動作確認用
├── site/config/_default/
│   ├── hugo.toml              ← baseURL設定済み
│   ├── params.toml            ← ga4_id を入力する ⚠️
│   └── menus.toml             ← ナビゲーション設定
├── site/static/
│   ├── css/main.css           ← メインCSS（Gear Patrol風デザイン）
│   ├── images/                ← 静的画像
│   └── robots.txt
├── site/content/
│   ├── about.md               ← Amazon審査必須
│   ├── privacy.md             ← Amazon審査必須
│   ├── contact.md             ← Amazon審査必須
│   └── articles/              ← 生成された記事（ファイル名: YYYYMMDDHH-slug.md）
└── .github/workflows/
    ├── deploy.yml             ← push → GitHub Pages 自動デプロイ
    ├── generate_articles.yml  ← 月水金9時JST 自動記事生成
    └── refresh_topics.yml     ← 日曜9時JST 自動トピック補充
```
