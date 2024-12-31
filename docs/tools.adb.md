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

# How adb works?
* TODO: