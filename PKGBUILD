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
b2sums=('8fbfdbf17df3b9e495d31392cb5658655284c77a8396babab6e6317a74022cb94d0156745654868ee22db6b15f84a541a9395af4851c15cbccb5d7ed72a53841')

package() {
	install -Dm755 main.py "${pkgdir}/usr/bin/download-yt-video"
}
