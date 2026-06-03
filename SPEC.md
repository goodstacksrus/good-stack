# GOOD STACK — システム仕様書

> **対象読者**: このプロジェクトを初めて触る方、または引き継いだ方  
> **目的**: GOOD STACK が何者で、どう動いて、どう使うかを一通り理解できるようにする

---

## 目次

1. [このアプリは何をするもの？](#1-このアプリは何をするもの)
2. [全体の仕組み（アーキテクチャ）](#2-全体の仕組みアーキテクチャ)
3. [使っている技術一覧](#3-使っている技術一覧)
4. [ファイル構成](#4-ファイル構成)
5. [初回セットアップ](#5-初回セットアップ)
6. [日常の使い方](#6-日常の使い方)
7. [自動化の仕組み（GitHub Actions）](#7-自動化の仕組みgithub-actions)
8. [記事の中身はどう作られるか](#8-記事の中身はどう作られるか)
9. [データの流れ](#9-データの流れ)
10. [よくあるエラーと対処法](#10-よくあるエラーと対処法)
11. [将来の計画（ロードマップ）](#11-将来の計画ロードマップ)

---

## 1. このアプリは何をするもの？

**GOOD STACK** は、AIが自動で記事を書いてウェブサイトに公開するシステムです。

### ひとことで言うと

> 「Amazonアフィリエイトで稼ぐための記事メディアを、AIが全自動で運営する」

### 具体的には

1. **テーマを決める**（例：「スマートプラグ おすすめ 節電」）
2. **AI（Gemini）が記事を書く** → Google検索で最新情報も参照できる
3. **写真サービス（Pexels）から画像を自動取得**して記事に付ける
4. **Hugoでウェブサイトに変換** → GitHub Pages で公開
5. **毎週自動で繰り返す**（GitHub Actions による定期実行）

### 公開されているサイト

- **URL**: https://goodstacksrus.github.io/good-stack/
- **GitHub**: https://github.com/goodstacksrus/good-stack

---

## 2. 全体の仕組み（アーキテクチャ）

```
┌─────────────────────────────────────────────────────┐
│                     ローカル PC                       │
│                                                     │
│  Python スクリプト                                   │
│  ┌────────────────┐   ① トピック取得    ┌──────────┐│
│  │ refresh_topics │ ←──────────────── │ Google  ││
│  │      .py       │                   │ Trends  ││
│  └────────────────┘                   └──────────┘│
│         │ ② トピック保存                            │
│         ▼                                          │
│  ┌────────────────────┐                            │
│  │ topic_registry.json│ ← 生成待ちトピックのリスト   │
│  └────────────────────┘                            │
│         │ ③ 次のトピックを取得                      │
│         ▼                                          │
│  ┌────────────────┐  ④ 記事文章を生成  ┌──────────┐│
│  │ local_generate │ ──────────────── →│  Gemini ││
│  │      .py       │ ←────────────────  │   API   ││
│  └────────────────┘                   └──────────┘│
│         │                      ⑤ 画像を取得        │
│         │              ┌──────────────────────────┐│
│         │              │       Pexels API         ││
│         │              └──────────────────────────┘│
│         │ ⑥ Markdownファイル生成                   │
│         ▼                                          │
│  ┌────────────────────────────────────┐            │
│  │ site/content/articles/記事名.md    │            │
│  └────────────────────────────────────┘            │
│         │ ⑦ Hugoでビルド                           │
│         ▼                                          │
│  ┌────────────────────┐                            │
│  │   site/public/     │ ← HTML/CSS/画像が生成される │
│  └────────────────────┘                            │
└─────────────────────────────────────────────────────┘
         │ ⑧ git push
         ▼
┌─────────────────────────────────────────────────────┐
│                    GitHub                           │
│  ┌──────────────────────────────────────────────┐  │
│  │ GitHub Actions（自動化）                      │  │
│  │  - 月・水・金：記事を自動生成                  │  │
│  │  - 日曜：トピックを自動補充                    │  │
│  │  - push のたび：GitHub Pages にデプロイ       │  │
│  └──────────────────────────────────────────────┘  │
│                    │                                │
│                    ▼                                │
│  ┌──────────────────────────────────────────────┐  │
│  │  GitHub Pages                                │  │
│  │  https://goodstacksrus.github.io/good-stack/ │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 3. 使っている技術一覧

| 役割 | 技術名 | なぜこれを使うか |
|---|---|---|
| AI 記事生成 | **Google Gemini 2.5 Flash API** | 高品質な文章を自動生成。Google検索との連携も可能 |
| トレンド取得 | **Google Trends（pytrends）** | 今何が検索されているかをリアルタイム取得 |
| 記事画像 | **Pexels API** | 商用利用可の高品質写真が無料で使い放題 |
| サイト構築 | **Hugo** | Markdownを即座に本格的なウェブサイトに変換する静的サイトジェネレーター |
| サイト公開 | **GitHub Pages** | GitHubのリポジトリをそのままウェブサイトとして無料公開 |
| 自動化 | **GitHub Actions** | スケジュール実行・CI/CD。月水金に記事を自動生成 |
| バリデーション | **Pydantic** | AIが返したJSONデータの型チェックと変換 |
| HTTP通信 | **httpx** | Pexels APIへの画像取得リクエスト |
| テスト | **pytest** | コードが正しく動くか自動検証 |
| 言語 | **Python 3.x** | スクリプト全体の実装言語 |

### APIキーが必要なサービス

| サービス | 取得先 | 無料枠 |
|---|---|---|
| Gemini API | https://aistudio.google.com/app/apikey | 1日60リクエスト程度 |
| Pexels API | https://www.pexels.com/api/ | 月200件（登録のみ・完全無料） |

---

## 4. ファイル構成

```
good-stack/
│
├── .env                    ← APIキーを書くファイル（非公開・Gitに含めない）
├── .env.example            ← .envのひな形（Gitに含まれる）
├── requirements.txt        ← 必要なPythonパッケージ一覧
├── topic_registry.json     ← 記事のネタ帳（自動生成・自動更新）
│
├── generator/              ← 記事生成の「エンジン」部分
│   ├── article_pipeline.py ← メインの処理フロー（全体の司令塔）
│   ├── gemini_client.py    ← GeminiへのAPI呼び出し
│   ├── image_client.py     ← PexelsへのAPI呼び出し
│   ├── markdown_writer.py  ← 記事をMarkdownファイルに書き出す
│   ├── models.py           ← 記事データの型定義（Pydantic）
│   ├── topic_registry.py   ← ネタ帳の読み書き管理
│   └── trend_client.py     ← Google Trendsからトピック取得
│
├── scripts/                ← ターミナルから実行するスクリプト
│   ├── local_generate.py   ← 記事を1本生成する（メインコマンド）
│   ├── refresh_topics.py   ← ネタ帳にトピックを補充する
│   ├── list_models.py      ← 使えるGeminiモデルを確認
│   └── test_api.py         ← APIキーの動作確認
│
├── site/                   ← Hugoサイト（ウェブサイト本体）
│   ├── config/             ← サイトの設定（URL、タイトル、メニューなど）
│   ├── content/            ← 記事ファイルの置き場所
│   │   └── articles/       ← ここに .md ファイルが溜まっていく
│   ├── layouts/            ← HTMLテンプレート（見た目の設計）
│   ├── static/             ← CSS・画像など静的ファイル
│   └── public/             ← Hugoがビルドした完成品（Gitignore推奨）
│
├── tests/                  ← 自動テスト（pytest）
│
└── .github/workflows/      ← GitHub Actions の定義ファイル
    ├── generate_articles.yml ← 月水金に記事を自動生成
    ├── refresh_topics.yml    ← 日曜にネタ帳を自動補充
    └── deploy.yml            ← pushのたびにGitHub Pagesにデプロイ
```

---

## 5. 初回セットアップ

### ステップ1: リポジトリをクローン

```powershell
git clone https://github.com/goodstacksrus/good-stack.git
cd good-stack
```

### ステップ2: Python仮想環境を作成・有効化

```powershell
python -m venv .venv
.venv\Scripts\activate
```

> プロンプトの先頭に `(.venv)` と表示されれば有効化できています。

### ステップ3: 依存パッケージをインストール

```powershell
pip install -r requirements.txt
```

### ステップ4: APIキーを設定する

`.env.example` をコピーして `.env` を作成：

```powershell
copy .env.example .env
```

作成した `.env` をテキストエディタで開いて、APIキーを入力：

```
GOOGLE_API_KEY=AIza...ここにGeminiのAPIキーを貼る...
LLM_MODEL=gemini-2.5-flash
PEXELS_API_KEY=...ここにPexelsのAPIキーを貼る...
```

### ステップ5: APIキーの動作確認

```powershell
python scripts\test_api.py
```

エラーが出なければセットアップ完了です。

### ステップ6: Hugoのインストール（初回のみ）

Hugoの公式サイト（https://gohugo.io/installation/）からインストール。  
インストール後、VSCodeを再起動して `hugo version` でバージョンが表示されれば成功。

---

## 6. 日常の使い方

### 作業開始時（毎回）

```powershell
cd C:\Users\oueno\venv\good-stack
.venv\Scripts\activate
```

### 記事を1本生成する

**パターンA: とにかく試したい（APIキー不要・モック）**
```powershell
python scripts\local_generate.py --mock
```
> AIを使わずダミー文章で即時生成。記事の構造確認に使う。

**パターンB: 通常生成**
```powershell
python scripts\local_generate.py
```
> GeminiがネタをレジストリからピックアップしてAI記事を生成。約30〜60秒。

**パターンC: テーマを自分で指定して生成**
```powershell
python scripts\local_generate.py --topic "スマートプラグ おすすめ 節電"
```

**パターンD: Google検索つき（最高品質・推奨）**
```powershell
python scripts\local_generate.py --topic "AirPods Pro ケース" --search
```
> 最新の製品情報・価格・レビューをGoogle検索してから執筆。約1〜2分。

### サイトをブラウザで確認する（別ターミナルで）

```powershell
cd site
hugo server --buildDrafts --buildFuture --navigateToChanged
```

ブラウザで **http://localhost:1313/good-stack/** を開く。  
記事を生成するたびにブラウザが自動でリロードされます。

### ネタ帳（topic_registry.json）を補充する

```powershell
# Google Trends + Gemini で自動取得（推奨）
python scripts\refresh_topics.py

# ジャンルを絞って取得
python scripts\refresh_topics.py --seeds "キャンプ アウトドア" "登山 ガジェット"

# トピックを手動で直接追加
python scripts\refresh_topics.py --add "iPhone 16 Pro ケース おすすめ"

# 追加せず結果だけ確認
python scripts\refresh_topics.py --dry-run
```

### 残りトピック数を確認する

```powershell
python -c "from generator.topic_registry import TopicRegistry; r=TopicRegistry(); print(f'残り: {r.pending_count()}件')"
```

### テストを実行する

```powershell
python -m pytest tests/ -v
```

---

## 7. 自動化の仕組み（GitHub Actions）

GitHub上のリポジトリで、3つのワークフローが自動実行されます。

### 記事自動生成（Generate Articles）

| 項目 | 内容 |
|---|---|
| **実行タイミング** | 月・水・金 午前9時JST |
| **やること** | 記事を1本生成 → commit → GitHub Pagesにデプロイ |
| **手動実行** | Actions タブ → Generate Articles → Run workflow |
| **設定画面** | topic（空欄なら自動選択）、use_mock（true/false） |

### トピック自動補充（Refresh Topics）

| 項目 | 内容 |
|---|---|
| **実行タイミング** | 毎週日曜 午前9時JST |
| **やること** | Google Trends + Gemini からトピックを取得してネタ帳に追加 |
| **手動実行** | Actions タブ → Refresh Topics → Run workflow |

### 自動デプロイ（Deploy）

| 項目 | 内容 |
|---|---|
| **実行タイミング** | mainブランチへのpush のたびに実行 |
| **やること** | Hugo でビルド → GitHub Pages に公開 |

### GitHub Secrets の設定（必須）

GitHub リポジトリの Settings → Secrets and variables → Actions から以下を登録：

| Secret 名 | 値 |
|---|---|
| `GOOGLE_API_KEY` | Gemini APIキー |
| `PEXELS_API_KEY` | Pexels APIキー |

---

## 8. 記事の中身はどう作られるか

### 記事の構造

AIが生成する記事は以下の構成で作られます：

```
記事ファイル（Markdown）
│
├── フロントマター（YAML）
│   ├── title:       記事タイトル
│   ├── slug:        URL（例: smart-plug-energy-saving）
│   ├── date:        生成日時
│   ├── description: 検索結果に表示される120〜160字の説明文
│   ├── tags:        タグ（3〜5個）
│   ├── categories:  カテゴリ（1〜2個）
│   └── image:       ヒーロー画像のURL（Pexelsから取得）
│
├── 導入文（イントロ）
│
├── セクション1〜7（H2見出し + 本文150〜300字）
│   └── セクション内に本文画像（2枚）
│
├── 購入ガイド（選び方のポイント）
│
├── アフィリエイトボタン（Amazon）
│
└── まとめ（コンクルージョン）
```

### ファイル名の規則

```
site/content/articles/2026051614-smart-plug-energy-saving.md
                       ──────────  ─────────────────────────
                       年月日時(4桁)  slug（URLに使われる）
```

- ファイル名の日時はソート用。URLは `slug:` フィールドで決まる
- 同じ日に複数記事を生成しても時刻で区別される

---

## 9. データの流れ

### topic_registry.json の仕組み

ネタ帳は JSON ファイルで、2つの状態を管理しています：

```json
{
  "pending": [
    "スマートプラグ おすすめ 節電",
    "AirPods Pro ケース 比較"
  ],
  "generated": [
    "Echo Dot 5 レビュー"
  ]
}
```

| 状態 | 意味 |
|---|---|
| `pending` | まだ記事化していないトピック（生成待ち） |
| `generated` | 記事を生成済みのトピック（再生成しない） |

### Gemini API への入力・出力

**入力（プロンプト）**:
- トピック名
- 記事の構成ルール（セクション数・文字数など）
- （--searchの場合）Google検索結果の抜粋

**出力（JSON）**:
```json
{
  "title": "スマートプラグ おすすめ5選【節電・電力管理に】",
  "slug": "smart-plug-energy-saving-top5",
  "description": "...",
  "tags": ["スマートプラグ", "節電", "スマートホーム"],
  "sections": [
    { "heading": "スマートプラグとは？", "content": "..." },
    ...
  ],
  "buying_guide": "...",
  "conclusion": "..."
}
```

---

## 10. よくあるエラーと対処法

| エラーメッセージ | 原因 | 対処 |
|---|---|---|
| `GOOGLE_API_KEY が見つからない` | `.env` が未作成 | `.env.example` をコピーして `.env` を作成しAPIキーを入力 |
| `429 RESOURCE_EXHAUSTED` | Gemini APIの無料枠を超えた | 時間をおくか、別のAPIキーを使用 |
| `404 NOT_FOUND` モデルが見つからない | モデル名が古い・廃止された | `python scripts\list_models.py` で確認し `.env` のモデル名を更新 |
| Hugo が `hugo: command not found` | Hugoが未インストール or PATHが通っていない | Hugoをインストールし、VSCodeを再起動 |
| 画像が表示されない | `PEXELS_API_KEY` が未設定 | `.env` に `PEXELS_API_KEY` を追加 |
| 記事がサイトに表示されない | 記事の `date:` が未来の日時になっている | 記事の `date:` を現在より過去の日時に修正 |
| CSSが当たっていない（画面が崩れる） | ブラウザのキャッシュが古い | Ctrl+Shift+R でハードリロード |
| GitHub Actionsが失敗する | Secrets が未登録 | GitHubのSettings → Secrets から `GOOGLE_API_KEY` と `PEXELS_API_KEY` を登録 |

---

## 11. 将来の計画（ロードマップ）

### Phase 1（完了済み）

- [x] Python記事生成エンジン
- [x] Gemini API連携（通常 + Google検索Grounding）
- [x] Pexels画像自動取得（ヒーロー1枚 + 本文2枚）
- [x] Hugo サイト構築（Gear Patrol風デザイン）
- [x] GitHub Actions（記事自動生成・トピック補充・デプロイ）
- [x] トレンドトピック自動補充（Google Trends + Gemini）
- [x] pytest テスト（11テスト全パス）

### Phase 2（進行中）

- [ ] GitHub Secrets に APIキーを登録（GitHub Actionsを本稼働させる）
- [ ] Google Analytics 4 の設定（アクセス解析）
- [ ] Google Search Console に登録（SEO強化）
- [ ] 記事20本以上を生成・公開

### Phase 3（今後）

- [ ] Amazonアソシエイトに申請・承認取得
- [ ] 記事へのAmazonアフィリエイトリンクを挿入
- [ ] 収益化開始

---

## 補足: よく使うコマンド早見表

```powershell
# 仮想環境の有効化（毎回必要）
.venv\Scripts\activate

# モックで記事生成（確認用・APIキー不要）
python scripts\local_generate.py --mock

# 通常の記事生成
python scripts\local_generate.py

# トピック指定 + Google検索つき生成（最高品質）
python scripts\local_generate.py --topic "テーマ" --search

# トピックを補充
python scripts\refresh_topics.py

# 残りトピック数を確認
python -c "from generator.topic_registry import TopicRegistry; r=TopicRegistry(); print(f'残り: {r.pending_count()}件')"

# Hugoサーバー起動（別ターミナルで）
cd site && hugo server --buildDrafts --buildFuture --navigateToChanged

# テスト実行
python -m pytest tests/ -v

# 使えるGeminiモデルを確認
python scripts\list_models.py
```

---

*この仕様書は `仕様書.md` として GOOD STACK プロジェクトルートに保存されています。*
