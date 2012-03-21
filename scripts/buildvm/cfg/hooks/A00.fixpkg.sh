#!/bin/sh
# Script to work around broken Debian packages.

if [ -e /usr/src/open-vm.tar.bz2 ]; then
    echo "*** WORKAROUND: expanding open-vm.tar.bz2 as root."
    cd /usr/src/
    tar -jxf open-vm.tar.bz2
fi

