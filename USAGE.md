# 使い方ガイド — GOOD STACK
```
# トピックを指定
python scripts\local_generate.py --topic "スマートプラグ おすすめ 節電" --search
```powershell
# ターミナルを別に開いてHugo開発サーバーを起動
cd site
hugo server --buildDrafts --buildFuture --navigateToChanged
```
---

## 前提条件（初回のみ）

```powershell
# 仮想環境を有効化（毎回必要）
cd C:\Users\oueno\venv\good-stack
.venv\Scripts\activate
```

`.env` に以下のキーが設定されていること：

```
GOOGLE_API_KEY=AIza...        # Gemini API（記事生成）
LLM_MODEL=gemini-2.5-flash
PEXELS_API_KEY=...            # Pexels API（記事画像・無料）
```

- Gemini APIキー取得先: https://aistudio.google.com/app/apikey
- Pexels APIキー取得先: https://www.pexels.com/api/（無料・登録のみ）

---

## 記事を生成する

生成された記事は `site/content/articles/YYYYMMDDHH-slug.md` の形式で保存されます。  
Pexels APIキーが設定されていれば**ヒーロー画像1枚＋本文内画像2枚**が自動で付きます。

### パターン① モック生成（APIキー不要・動作確認用）

```powershell
# レジストリから次のトピックを自動選択して生成
python scripts\local_generate.py --mock

# トピックを指定して生成
python scripts\local_generate.py --topic "Echo Dot ケース おすすめ" --mock
```

- AIを使わずテンプレート文章で即時生成（画像は付かない）
- 表示・構造の確認に使う

### パターン② Gemini生成（通常）

```powershell
# レジストリから次のトピックを自動選択
python scripts\local_generate.py

# トピックを指定
python scripts\local_generate.py --topic "スマートプラグ おすすめ 節電"
```

- Gemini APIが記事を執筆、Pexelsから画像を自動取得
- 所要時間: 30秒〜1分

### パターン③ Google検索つき生成（最高品質）

```powershell
# レジストリから次のトピックを自動選択
python scripts\local_generate.py --search

# トピックを指定
python scripts\local_generate.py --topic "スマートプラグ おすすめ 節電" --search
```

- Google検索で最新の製品情報・価格・レビューを取得してから執筆
- Pexelsから画像を自動取得（ヒーロー1枚＋本文2枚）
- 所要時間: 1〜2分
- 流れ: `Google検索中...` → `記事を生成中...` → `Images fetched: 3 photos` → 完了

### フラグのまとめ

| フラグ | 意味 |
|---|---|
| なし | Geminiで通常生成・画像付き |
| `--mock` | APIなし・テンプレートで即時生成（画像なし） |
| `--search` | Google検索で最新情報を取得してから生成・画像付き |
| `--topic "..."` | トピックを直接指定（省略するとレジストリから自動選択） |

---

## サイトをローカルで確認する

```powershell
# ターミナルを別に開いてHugo開発サーバーを起動
cd site
hugo server --buildDrafts --buildFuture --navigateToChanged
```

ブラウザで **http://localhost:1313/good-stack/** を開く。

記事を生成するたびにブラウザが**自動でリロード**される。

---

## 記事ファイルの構成

生成されたMarkdownファイルのフロントマター例：

```yaml
---
title: Echo Show 15 おすすめアクセサリーまとめ
slug: echo-show-15-accessories-guide
date: '2026-05-16T14:30:00'   # 生成した時刻（秒単位）
description: ...
tags: [...]
categories: [...]
image: https://images.pexels.com/...  # ヒーロー画像URL
draft: false
---
```

- ファイル名: `2026051614-echo-show-15-accessories-guide.md`（年月日時+スラッグ）
- URLは `slug:` フィールドで決まるのでファイル名の日時はURLに影響しない
- 同日に複数記事を生成しても時刻で順番が区別される

---

## トピックを管理する

トピックは `topic_registry.json`（自動生成）で管理される。

```powershell
# 残りトピック数を確認
python -c "from generator.topic_registry import TopicRegistry; r=TopicRegistry(); print(f'残り: {r.pending_count()}件')"
```

### トピックを補充する（トレンドから自動取得）

```powershell
# Google Trends + Gemini grounding の両方から取得（推奨）
python scripts\refresh_topics.py

# Geminiのみ（Google Trendsが遅い・エラーの時）
python scripts\refresh_topics.py --source gemini

# ジャンルを指定して絞り込む（Google Trends・Gemini 両方に適用）
python scripts\refresh_topics.py --seeds "キャンプ アウトドア" "登山 ガジェット"

# 追加せず取得結果だけ確認する
python scripts\refresh_topics.py --dry-run

# pending が5件以下の時だけ補充する
python scripts\refresh_topics.py --min-pending 5

# キャンプ・アウトドア系に絞る
python scripts/refresh_topics.py --seeds "キャンプ アウトドア" "登山 ガジェット"

# スマホ・iPhone系に絞る
python scripts/refresh_topics.py --seeds "iPhone アクセサリー" "Android スマホ"

# 季節テーマで絞る（夏家電など）
python scripts/refresh_topics.py --seeds "夏 家電" "節電 グッズ"

# 確認してから追加
python scripts/refresh_topics.py --seeds "キャンプ" --dry-run

# Geminiだけ（Google Trendsが遅い時）
python scripts/refresh_topics.py --source gemini --seeds "キャンプ"
```

### トピックを直接追加する

```powershell
# 任意のトピックを直接追加
python scripts\refresh_topics.py --add "iPhone 16 Pro ケース おすすめ"

# 複数まとめて追加
python scripts\refresh_topics.py --add "iPad Air スタンド" "AirPods ケース 比較"

# 追加前に確認したい場合
python scripts\refresh_topics.py --add "新しいトピック" --dry-run
```

| フラグ | 意味 |
|---|---|
| なし | Google Trends + Gemini 両方からトピックを取得して追加 |
| `--source gemini` | Gemini groundingのみ |
| `--source google` | Google Trendsのみ |
| `--seeds "..."` | 指定キーワードのジャンルに絞り込む（両方に適用） |
| `--add "..."` | トピックを直接指定して追加（トレンド取得なし） |
| `--dry-run` | 追加せず結果だけ表示 |
| `--min-pending N` | pending が N 件以上あればスキップ |

---

## テストを実行する

```powershell
python -m pytest tests/ -v
```

---

## 利用可能なGeminiモデルを確認する

```powershell
python scripts\list_models.py
```

`.env` の `LLM_MODEL=` にモデル名を設定する（`models/` プレフィックスは不要）。

---

## GitHub Actionsで自動生成する（公開後）

### 記事生成（Generate Articles）

GitHubのリポジトリページ → **Actions** タブ → **Generate Articles** → **Run workflow**

| 入力欄 | 説明 |
|---|---|
| topic | 空欄なら自動選択、入力すると指定トピックで生成 |
| use_mock | `true` にするとAPIキー不要のモック生成 |

スケジュール自動実行: **月・水・金 午前9時JST**

### トピック補充（Refresh Topics）

GitHubのリポジトリページ → **Actions** タブ → **Refresh Topics** → **Run workflow**

| 入力欄 | 説明 |
|---|---|
| source | `both`（デフォルト）/ `gemini` / `google` |
| min_pending | pending がこの件数以上なら補充をスキップ（デフォルト: 5） |

スケジュール自動実行: **毎週日曜 午前9時JST**

GitHub Secrets に `GOOGLE_API_KEY` と `PEXELS_API_KEY` の両方を登録しておくこと。

---

## よくあるエラーと対処

| エラー | 原因 | 対処 |
|---|---|---|
| `GOOGLE_API_KEY` が見つからない | `.env` が未作成 | `.env.example` をコピーして `.env` を作成 |
| `429 RESOURCE_EXHAUSTED` limit:0 | APIキーの無料枠が有効でない | 別のAPIキーを発行するか課金設定を確認 |
| `404 NOT_FOUND` モデルが見つからない | モデル名が古い | `python scripts\list_models.py` で確認して `.env` を更新 |
| Hugoが認識されない | PATHが未更新 | VSCodeを再起動してから試す |
| 画像が表示されない | `PEXELS_API_KEY` 未設定 | `.env` に `PEXELS_API_KEY` を追加 |
| 記事が表示されない | 日時が未来になっている | 記事の `date:` を現在時刻より過去に修正 |
| CSS が反映されない（Chrome） | ブラウザキャッシュが古い | F12→更新ボタン右クリック→「キャッシュの消去とハード再読み込み」 |
| CSS が反映されない | Hugoサーバーを再起動していない | Ctrl+C で止めて再起動 |
| CSSが完全に読み込まれない（404） | CSSリンクが本番URLを指している | `head.html` で `absURL` を使わず `relURL` を使う（修正済み） |
| 記事ページにhero画像・パンくず・タグが出ない | `_default/page.html` が `single.html` より優先されている | `page.html` を削除する（修正済み） |
| 記事が表示されない（夜間生成） | 生成時刻が未来扱いになる | `--buildFuture` フラグ付きでサーバー起動（デフォルト済み） |
