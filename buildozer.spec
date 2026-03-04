[app]
title = Resizer Pro
package.name = resizerfoto
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk-bundle

# Library yang dibutuhkan
requirements = python3,kivy==2.2.1,pillow,kivymd==1.1.1

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

# --- BAGIAN PENTING YANG TADI HILANG ---
android.accept_sdk_license = True
p4a.branch = master
# ---------------------------------------

android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
