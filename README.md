# auto-download-pixiv-bookmark-images

pixivのブックマーク画像を全部ダウンロードしてくるやつ

注意：pixivpyは公式のAPIではないのでどうなっても知らないです, 誰も責任はとりません. ご了承ください.

Qiitaを書きましただいたい[これ](https://qiita.com/addtobasic/items/e17d0a5c7fd226714f3c)に書いています.

# Requirement
* python3
* pip3
* python3-venv

# Setup
```bash
$ git clone https://github.com/addtobasic/auto-download-pixiv-bookmark-images.git
$ cd auto-download-pixiv-bookmark-images
$ python3 -m venv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt
```

## Start the download
download.pyの15行目に自身のpixivのメールアドレスとパスワードを入れ, ターミナルで以下のコマンドを実行してください.

```bash
$ cd auto-download-pixiv-bookmark-images
$ python3 download.py
```

# References
* https://github.com/upbit/pixivpy
* https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde
* https://qiita.com/perlverity/items/a6bd388d96cb4ce69692
