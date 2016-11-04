set -xe
git submodule init
git submodule update --depth 1
cp build/core/root.mk Makefile

cd build
git clone --depth 1 https://android.googlesource.com/platform/build/soong
git clone --depth 1 https://android.googlesource.com/platform/build/blueprint
cd -
# http://stackoverflow.com/a/37629211/1027966
ln -s build/soong/bootstrap.bash
ln -s build/soong/Android.bp
