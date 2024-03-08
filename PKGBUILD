# Maintainer: Ivan <megagoodman@duck.com>
pkgname='download-yt-video'
pkgver=1.0
pkgrel=1
pkgdesc='YouTube download helper'
arch=('any')
url='https://github.com/Tula-gingerbread/download-youtube-video'
# no license
depends=('python-pytube')
source=("file://$srcdir/main.py")
sha256sums=('82ebd836d956daef26b06865b87942201e00a2b4c6d35fbfccc944d7498ced57')

package() {
	install -Dm755 main.py "$pkgdir/usr/bin/download-yt-video"
}
