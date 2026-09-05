https://developer.android.com/tools/adb

* Android Debug Bridge (adb)
  * := CL tool /
    * lets you -- communicate with a -- device 
    * -- facilitates a -- variety of device actions (_Example:_ installing and debugging apps) 
    * provides -- access to a -- Unix shell
      * uses
        * run a variety of commands | device 
  * == client-server program /
    * == 
      * client
        * sends commands
        * runs | your development machine
        * You can invoke a client from a command-line terminal by issuing an adb command.
      * daemon (adbd)
        * runs commands | device
        * runs -- as a -- background process | EACH device
      * server
        * manages communication between the client -- & the -- daemon
        * runs -- as a -- background process | your development machine
  * 👀included | Android SDK Platform Tools package 👀
    * see | `$ANDROID_HOME/platform-tools/`
  * if you are using Android Studio -> 
    * Android Studio handles the
      * packaging
      * installation of the app
    * ⚠️you do NOT need to use directly adb ⚠️

# How adb works?
* TODO:

# Install an app 
* allows
  * installing an APK |
    * emulator or
    * connected devices

* 
    ```
    adb install path_to_apk
    ```
  * `-t`
    * uses
      * install a test APK
  * `install-multiple`
    * uses
      * install MULTIPLE APKs
    * use cases
      * you download ALL the APKs -- for a -- specific device / your app -- from the -- Play Console &
      * want to install them | emulator or physical device


# Set up port forwarding
* TODO: