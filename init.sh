set -xe

# clone a repo only if it doesn't exist yet.
# allows you to rerun this script without fail.
check_clone() {
  dir=$(basename $1)
  if [ ! -d $dir ]; then
    echo "cloning $1"
    git clone --depth 1 $1
  fi
}

git submodule init
git submodule update --depth 1
cp build/core/root.mk Makefile

cd build
check_clone https://android.googlesource.com/platform/build/soong
check_clone https://android.googlesource.com/platform/build/blueprint
check_clone https://android.googlesource.com/platform/build/kati
cd -
# http://stackoverflow.com/a/37629211/1027966
ln -sf build/soong/bootstrap.bash
ln -sf build/soong/Android.bp
