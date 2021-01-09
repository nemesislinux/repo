name=busybox
desc=Utilities for rescue and embedded systems

sources=("https://www.busybox.net/downloads/busybox-$RLVERSION.tar.bz2")

configure() {
    cd "busybox-$RLVERSION"

    make defconfig
}

build() {
    cd "busybox-$RLVERSION"

    make $MAKEOPTS
}

install() {
    mkdir "$PREFIX/bin"

    mv "busybox-$RLVERSION/busybox" "$PREFIX/bin/busybox"

    cd "$PREFIX/bin"
    ./busybox --install -s .
}
