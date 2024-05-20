[buildozer]
# Buildozer configurations

log_level = 2
fetch_retries = 3
fetch_timeout = 30
package.source = android
warn_on_root = 1

[app]
# Application configurations

title = Phone Price App
package.name = phonepriceapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,numpy,joblib
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.1
fullscreen = 0
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
