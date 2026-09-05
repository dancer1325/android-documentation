https://developer.android.com/tools/sdkmanager

* `sdkmanager`
  * := CL tool / 
    * lets you, for the Android SDK,
      * view,
      * install,
      * update,
      * uninstall packages 
    * 👀if you're using Android Studio -> you do NOT need to use it 👀
    * built-in | [Android SDK CL tool](tools.md)
  * steps to install
    * download [from here](https://developer.android.com/studio#command-line-tools-only)
    * create a folder `cmdline-tools/latest/` | `ANDROID_HOME` 
    * copy the downloaded content | `ANDROID_HOME/cmdline-tools/latest/`
    * `export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin` | your environment variable
    * `sdkmanager --version`
      * check the installation works properly

## Usage
* TODO: