#!/bin/sh
set -e
D="$(realpath $(dirname $0))"
V="$($D/check-update.sh)"
T="$(mktemp -d /tmp/checkoutXXXXXX)"
cd "$T"
git clone https://gerrit.googlesource.com/git-repo
cd git-repo
git archive -o repo-"$V".tar --prefix repo-"$V"/ "v$V"
zstd --ultra -22 -f --rm repo-"$V".tar
mv -f repo-"$V".tar.zst "$D"/
cd "$D"
rm -rf "$T"
