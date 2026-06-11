[app]
title = PTRAP
package.name = ptrap
package.domain = org.ptrap
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.0

# تم تحديث النسخ هنا لضمان التوافق التام
requirements = python3, kivy==2.3.0, kivymd==1.1.1, pillow, sqlite3

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
icon.filename = assets/logo.png
presplash.filename = assets/logo.png

[buildozer]
log_level = 2
warn_on_root = 1
