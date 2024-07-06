[app]

# Title of your application
title = MelHad Payment App

# Package name
package.name = melhadpaymentapp

# Package domain (needed for android/ios packaging)
package.domain = org.melhad

# Source code where the main.py is located
source.dir = Payment-Processor-System-/payment_app

# Application versioning
version = 0.1

# Application requirements
requirements = python3, kivy, cython, flask, flask_sqlalchemy, pyyaml, python-dotenv

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# The format used to package the app for distribution
android.release_artifact = aab

# Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png

# Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# Supported screen orientations
orientation = portrait

# Indicate if the application should be fullscreen or not
fullscreen = 1

# Supported platforms
# Uncomment the platform(s) you want to target
# android.api = 33
# android.minapi = 21
# android.ndk = 25b
# android.gradle_dependencies = 'com.google.firebase:firebase-analytics:17.2.1'
# android.gradle_version = 7.2
