# Reflex Sample - Modern Web App with Python

## 概要
このプロジェクトは、Reflexフレームワークを使用して構築されたサンプルアプリケーションです。Pythonのみで美しくインタラクティブなウェブアプリケーションを構築できることを示しています。

## 機能

### カウンターアプリケーション
- モダンなUIデザインのシンプルなカウンターアプリケーション
- 増加・減少ボタンによる状態管理
- Tailwind CSSによるスタイリング

### シンデレラストーリーのランディングページ
- Reflexをテーマにしたシンデレラストーリーのランディングページ
- レスポンシブデザイン（モバイル・タブレット・デスクトップ対応）
- 美しいグラデーションと画像を使用したセクション
- 流れるようなストーリーテリング形式のコンテンツ

## 技術スタック
- **フレームワーク**: Reflex (Python Web App Framework)
- **スタイリング**: Tailwind CSS
- **状態管理**: Reflexの組み込み状態管理

## 開発環境

- M1 Mac
- Docker Compose

## セットアップ方法

### Dockerを使用する場合

```bash
# リポジトリをクローン
git clone [リポジトリURL]
cd reflex-sample

# Dockerコンテナを起動
docker-compose up
```

### ローカルで実行する場合

```bash
# リポジトリをクローン
git clone [リポジトリURL]
cd reflex-sample

# 環境をセットアップ
pip install -r requirements.txt

# 開発サーバーを起動
reflex run
```

## 使用方法

開発サーバーが起動したら、以下のURLにアクセスしてください：

- カウンターアプリケーション: http://localhost:3000
- シンデレラストーリーのランディングページ: http://localhost:3000/lp

## プロジェクト構造

```
reflex-sample/
├── reflex_sample/
│   └── reflex_sample.py   # メインアプリケーションコード
└── rxconfig.py            # Reflex設定ファイル
```

## ライセンス

[ライセンス情報を記載]
