# Maintainer: Ivan <megagoodman@duck.com>
pkgname='download-yt-video'
pkgver=1.1
pkgrel=4
pkgdesc='YouTube download helper'
arch=('any')
url='https://github.com/Tula-gingerbread/download-youtube-video'
# no license
depends=('python-pytube')
optdepends=('ffmpeg: converting to mp3')
source=("file://${srcdir}/main.py")
sha256sums=('7331c41f546520fc8eda047b5a05cf63836d8bbb022a079adf0579b325c339f5')

package() {
	install -Dm755 main.py "${pkgdir}/usr/bin/download-yt-video"
}
