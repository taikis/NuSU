<h2>
<img src="./assets/title-banner.png" style="width=100%" alt="NuSU">
</h2>

[English doc available here](./README-en.md)

### 概要

NuSUはハーフカメラ用の画像分割ソフトです。フルフレーム（36mm × 24mm）で現像された画像を、一括でハーフサイズに分割します。

### 使い方

#### 1. ダウンロード

[こちら](https://github.com/taikis/NuSU/releases)から最新版をダウンロードしてください。

#### 2. 起動

適当なフォルダにおき、アプリを起動してください。インストールは不要です。

#### 3. 画像の選択

画像を選択してください。複数選択することもできます。

#### 4. 画像の分割

「Cut & Save」ボタンを押してください。選択した画像が、任意のフォルダにハーフサイズで保存されます。

### 開発

#### パッケージ化

```sh
pip install -r requirements.txt
```

```sh
flet pack source/gui.py --icon 'assets/icon.png' --name NuSU --product-name NuSU --copyright 'Taiki Sugawara'
```