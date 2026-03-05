[app]
title = Resizer Pro
package.name = resizerfoto
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,pillow,kivymd==1.1.1
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
