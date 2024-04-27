# Maintainer: Ivan <megagoodman@duck.com>
pkgname='download-yt-video'
pkgver=1.2
pkgrel=2
pkgdesc='YouTube download helper'
arch=('any')
url='https://github.com/Tula-gingerbread/download-youtube-video'
# no license
depends=('python-pytube')
optdepends=('ffmpeg: converting to mp3')
source=("file://${srcdir}/main.py")
b2sums=('a1d5ee245db3849945fa4080d643b0eb70f7ae637eebb1bc2413806a74eb93d0d273a8c8d886d2d72d09b3c640dd0a40680ba637c62f1e9ea05bfca808cd5bb2')

package() {
	install -Dm755 main.py "${pkgdir}/usr/bin/download-yt-video"
}
