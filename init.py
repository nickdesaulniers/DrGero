import subprocess

repos = [
    (
        "https://android.googlesource.com/platform/frameworks/native",
        "frameworks/native"
    ), (
        "https://android.googlesource.com/platform/build",
        "build"
    ), (
        "https://android.googlesource.com/device/lge/hammerhead",
        "device/lge/hammerhead"
    ), (
        "https://android.googlesource.com/device/lge/hammerhead-kernel",
        "device/lge/hammerhead-kernel"
    )
]

cmds = [
    "git",
    "submodule",
    "add",
    "--depth",
    "1"
]

subprocess.call(["git", "init"])
for url, path in repos:
    subprocess.call(cmds + [url, path])
subprocess.call(["cp", "build/core/root.mk", "Makefile"])
