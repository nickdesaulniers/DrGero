set -xe
source build/envsetup.sh
lunch aosp_hammerhead-userdebug
make -j bootimage
