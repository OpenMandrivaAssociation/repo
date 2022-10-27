#!/bin/sh
git ls-remote --tags https://gerrit.googlesource.com/git-repo 2>/dev/null |awk '{ print $2; }'  |grep -v '\^{}' |sed -e 's,refs/tags/v,,' |sort -V |tail -n1
