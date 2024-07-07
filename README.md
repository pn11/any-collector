# A exif-watermark Flet app

Exif から取り出した情報を写真に書き込みたい。Android とかでちゃんと動くようにやりたいことをやるには 現状の Flet では難しそう。

- Pillow などは Flet 0.x ではネイティブで動かない。 Pure な Python を謳っている Willow には文字を重ねる方法はなさそう。
- Flet の Canvas には画像を読み込めなそう。たぶん Flutter ならできる。
  - まあ1ピクセルずつ読み込めばできないことはないかもしれないが、保存する方法が用意されてなさそう。おえかきしても保存できないじゃん！
  - Willow に突っ込めばもしかしたらいける？
  - と思ったけど、データのやり取りが Flutter 側に隠蔽されていてそうで見れない。
- Flet の Stack を使えば重ねられるが、それを画像として保存する方法がない。ユーザーがスクショを撮ればかろうじて実現できるが、画質が下がる。

初めて Flet を触った感想として、めちゃくちゃ簡単に作り始められるというのは分かったけど、ちょっと凝ったことをしようとすると (といっても大したことはしようとしていないと思うが)、すぐにネイティブで動かないということになりそうだった。デスクトップで動けば良いならこれで全然あり。

## 動かし方

### デバッグモード

```sh
flet run .
```

または

```sh
flet run main.py
```

### ビルド

### Mac

```sh
flet build macos
```

#### Android

```sh
flet build apk
```

なお、Mac 上で micoromamba で Flet の環境を作っていたが、 ld が Mac のものではなく micromamba 由来のものとなっていたため `ld: unknown option: -Xlinker` というエラーが出ていた。 conda など同じような環境の人は注意。 `/usr/bin/ld` を優先するようにするため、

```sh
unlink /_YOUR_MICROMAMBA_ENV_/bin/ld
ln -s /usr/bin/ld /_YOUR_MICROMAMBA_ENV_/bin/ld 
micromamba deactivate
/_YOUR_MICROMAMBA_ENV_/bin/flet build macos
```

などとすればできた。(`export PATH=/usr/bin:$PATH` ではだめだった)  
cf. <https://github.com/flutter/flutter/issues/137250#issuecomment-1877803808>
