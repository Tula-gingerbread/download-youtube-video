# Maintainer: Ivan <megagoodman@duck.com>
pkgname='download-yt-video'
pkgver=1.1
pkgrel=3
pkgdesc='YouTube download helper'
arch=('any')
url='https://github.com/Tula-gingerbread/download-youtube-video'
# no license
depends=('python-pytube')
optdepends=('ffmpeg: converting to mp3')
source=("file://$srcdir/main.py")
sha256sums=('89415488c1ccf5376832b784e29d25f1bb470e303174f538d95de98197978d32')

package() {
	install -Dm755 main.py "$pkgdir/usr/bin/download-yt-video"
}
