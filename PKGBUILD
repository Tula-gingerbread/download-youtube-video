# Maintainer: Ivan <megagoodman@duck.com>
pkgname='download-yt-video'
pkgver=1.1
pkgrel=2
pkgdesc='YouTube download helper'
arch=('any')
url='https://github.com/Tula-gingerbread/download-youtube-video'
# no license
depends=('python-pytube')
optdepends=('ffmpeg: converting to mp3')
source=("file://$srcdir/main.py")
sha256sums=('bd0f5aed164c56ec7435566232e8be19f781e86c6e7c01bbd51ce562310276a0')

package() {
	install -Dm755 main.py "$pkgdir/usr/bin/download-yt-video"
}

