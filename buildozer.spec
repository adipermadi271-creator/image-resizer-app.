[app]
title = Pengubah Resolusi
package.name = resizerfoto
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Persyaratan Library
requirements = python3,kivy==2.2.1,pillow,kivymd

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# IZIN AKSES (Penting agar bisa baca galeri)
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# Ikon Aplikasi (Opsional, jika ada file icon.png)
#icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
