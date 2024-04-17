# Maintainer: Ivan <megagoodman@duck.com>
pkgname='download-yt-video'
pkgver=1.2
pkgrel=1
pkgdesc='YouTube download helper'
arch=('any')
url='https://github.com/Tula-gingerbread/download-youtube-video'
# no license
depends=('python-pytube')
optdepends=('ffmpeg: converting to mp3')
source=("file://${srcdir}/main.py")
b2sums=("171ad8d32bfef078c95b584f2f6e1323373ecfd0919ffe99d84ef5f4c2ae7fdec6637cede113794f1b30f8d486a4ff2ed0bcd40a1030f05bd94cbe6d7f528f9d")

package() {
	install -Dm755 main.py "${pkgdir}/usr/bin/download-yt-video"
}
