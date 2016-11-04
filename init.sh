set -xe
git submodule init
git submodule update --depth 1
cp build/core/root.mk Makefile
