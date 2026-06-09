[app]
title = PTRAP
package.name = ptrap
package.domain = org.ptrap
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sqlite3
icon.filename = assets/logo.png
presplash.filename = assets/logo.png
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
