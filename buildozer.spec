[app]
title = Balochi Word Quest
package.name = balochiwordquest
package.domain = org.inamiiartistry
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,mp3,wav,ttf,json
source.exclude_dirs = .git,.github,bin,.buildozer
version = 0.1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = VIBRATE
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
