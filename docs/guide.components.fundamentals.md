https://developer.android.com/guide/components/fundamentals

* languages to write Android apps
  * Kotlin,
  * Java,
  * C++

* 👀your code + data + resource files -- are compiled by Android SDK tools into an -> APK or Android App Bundle 👀

* Android package
  * == archive "*.apk" file / contains
    * Android app ( / required | runtime)
  * uses
    * install the app
      * -> distributed -- through -- Google Play

* Android App Bundle
  * == archive "*.aab" file / contains
    * Android app project + additional metadata ( / NOT required | runtime)
  * publishing format -> 
    * can NOT be installed | Android devices
    * defers | later stage
      * APK generation
      * signing to

* EACH Android app lives | 👀its own security sandbox👀 / -- protected by the -- Android security features
  * Android OS == multi-user Linux system / EACH app != user
  * the system -- assigns, by default -- 1! Linux user ID / EACH app
    * -- used ONLY by the -- system
      * _Example:_ system sets permissions | ALL app's files -> ONLY the user ID / assigned to that app -- can access -- them
    * unknown to the app 
  * OWN VM / EACH process
    * -> app's code -- runs in isolation from -- other apps
  * EVERY app runs | its OWN Linux process
    * if any of the app's components need to be executed -> Android system starts the process
    * if the process NO longer needed OR system MUST recover memory -- for -- other apps -> Linux process shuts down

* Android system implements the <em>principle of least privilege</em>
  * == EACH app, by default, -- has access ONLY to the -- components / requireD to do its work
  * -> very secure environment

* ways / app can share data & can access system services
  * arrange for 2 apps / share the SAME Linux user ID
    * -> they are -- able to access -- each other's files
    * if apps / same user ID & arrange to run | same Linux process & share the same VM -> conserve system resources 
    * sign the apps -- via the -- same certificate
  * app -- can request permission to access -- device data (_Example:_ device's location, camera, and Bluetooth connection) 
    * requirements
      * user explicitly grant these permissions

* main concepts | this documentation
  * core framework components / define your app
  * `AndroidManifest.xml`
  * Resources

# App components

* 👀== Android app's building blocks 👀 /
  * some -- depend on -- others
  * == entry point -- through which the -- system or a user can enter your app
* 👀Android app -- due to Android system design, can start -- another app’s component 👀
  * _Example:_ if you want the user to capture a photo with the device camera (NORMALLY are apps ALREADY for it) & it's using your app -> your app can use those aps (instead of developing an activity to capture a photo)

* types
  * have !=
    * purpose
    * lifecycle (== how a component is created and destroyed) 
  * **Activities**
    * == entry point -- for interacting with the -- user
    * UI == 1! screen
      * _Example:_ | email app, 
        * activity / shows a list of new emails,
        * another activity / compose an email,
        * another activity -- for -- reading emails
    * activities work together, BUT they are independent of the others
    * app1 -- can start, via Android system -- app2's activity
      * _Example:_ email app -- start, to send a picture, a -- camera app's activity
    * allow, about interactions system -- & -- app
      * track of what the user currently cares about == what is on-screen
        * -> system keeps running the process / hosts the activity
      * know previously processes / contain stopped activities
        * Reason: 🧠user may return to & prioritize those processes 🧠
      * help the app can handle its process killed
        * -> user can return to activities / restore their previous state
      * implement user flows between each app
    * way to implement an activity
      * subclass of the `Activity`class
    * see [Introduction to activities](guide.components.activities.intro-activities.md)
  * **Services**
    * == general-purpose entry point -- for -- keeping an app running | background
      * uses
        * perform
          * long-running operations
          * work for remote processes
      * use cases
        * higher-level system concepts
          * _Example:_ Live wallpapers, notification listeners, screen savers, input methods, accessibility services, ...
      * _Example:_ service can play music | background, WHILE user is in a different app 
    * 👀does NOT provide a UI 👀
    * ANOTHER component (_Example:_ activity) -- can 
      * start a -- service or
      * bind to -- it
    * types / tell the system -- how to manage an -- app
      * started services
        * keep them running | UNTIL their work is completed
        * types -- based on -- system handle
          * user is directly aware of handling
            * _Example:_ Music playback 
            * -> 
              * communication with the user -- via -- notifications
              * system prioritizes keeping that service's process running
          * regular background service
            * user is NOT directly aware of -> system has MORE freedom in managing its process
              * _Example:_ system could kill it, restart it sometime later, ...
      * bound services
        * run because some other app needs it
          * == system knows there is a dependency between these processes
          * _Example:_ if process A -- is bound to a -- process B's service -> system knows that it needs to keep process B & its service running 
        * provides an API -- to -- another process system
    * way to implement a service
      * subclass of `Service`
    * see [Services overview](develop.background-work.services.md)
    * if your app -- targets Android v5.0+ (API level v21+) -> use `JobScheduler`
      * conserve battery -- via, using `Doze`, optimally -- scheduling jobs
  * **Broadcast receivers**
    * == entry point -- to the -- app /
      * 👀 system -- can deliver broadcasts to -- apps / EVEN are NOT currently running 👀
        * -> app -- can respond to -- system-wide broadcast announcements 
        * == gateway -- to -- other components
          * -> take in account security implications 
    * _Example:_ app schedule an alarm == app NOT remain running | UNTIL the alarm goes off
    * origin
      * from the system
        * _Example:_ broadcast -- announcing that the -- screen is turned off / battery is low / picture is captured
      * from the Apps
        * _Example:_ let other apps know / some data is downloaded | device
    * NOT display a UI
      * ALTHOUGH, they can create a status bar notification
    * way to implement it
      * subclass of `BroadcastReceiver` / EACH broadcast == `Intent` object
  * **Content providers**
    * manages a shared set of app data / 
      * you can store | ANY location / your app can access (_Example:_ file system, SQLite database, web, ...)
        * -> can be read & write
      * if it permits it -> other apps can query or modify the data
    * _Example:_ content provider / manages the user's contact information
      * -- provided by -- Android system
    * != abstraction on a database
      * Reason: 🧠 != core purpose 🧠
    * | system point of view
      * == entry point into an app -- for -- publishing named data items / identified by a URI scheme
        * -> app -- decide how to --
          * map its data -- to a -- URI namespace
          * hand out those URIs -- to other -- entities 
      * system can manage about an app
        * -- assigning a URI, to an -- app
          * Reason: 🧠app NOT required to remain running 🧠
            * == | apps NOT running, URIs can persist
        * URIs -- provide an -- important fine-grained security model 
          * _Example:_ app can place the image's URI | clipboard, BUT its content provider locked up
            * -> second app -- tries, via temporary <i>URI permission grant</i>, to access -- that URI | clipboard
    * way to implement it
      * subclass of `ContentProvider` / implement a standard set of APIs -- to enable -- other apps to perform
        transactions
    * see [Content providers](guide.topics.providers.content-providers.md)

* if the system starts a component & app NOT YET running -> starts the process for that app & instantiate the classes / needed for the component
  * _Example:_ if your app starts the activity | camera app / captures a photo -> activity runs | process -- belonged to the -- camera app (❌NOT | your app's process❌)
  * ⚠️== Android apps do NOT have 1! entry point ⚠️
    * == there's NO `main()` function

* EACH app runs | SEPARATE process / file permissions -- restrict access to -- other apps
  * 👀-> your app -- can NOT DIRECTLY activate an -- another app's component 👀
  * steps to activate another app's component
    * from the app -- deliver a message, specifying your intent to start a particular component, to the -- Android system  
    * Android system activates the component for you
      * == Android system manage the activation of app's components 

## Activate components
* TODO:

# `AndroidManifest.xml`
* == app's <em>manifest file</em>
  * placed | root of the app project directory
  * uses
    * 👀declare ALL app's components 👀
      * == components & required device features -- for -- your app
      * ⚠️Activities, services, & content providers / NOT declared | manifest -> NOT visible | system == can NEVER run ⚠️
      * broadcast receivers NOT need to be declared | manifest & run | your app
        * Reason: 🧠 can be created dynamically in code -- via -- 
          * <a href="/reference/android/content/BroadcastReceiver">BroadcastReceiver</a> objects
          * registered them -- via -- <a href="/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter)">registerReceiver()</a>
    * identifies any user permissions -- required by the -- app
      * _Example:_ internet access, read-access to the user's contacts
    * Declares the minimum API level / required by the app
      * -- based on the -- APIs used by the app
    * Declares hardware and software features / used or required -- by the -- app
      * _Example:_ camera, Bluetooth services, multitouch screen
    * Declares API libraries / app -- needs to be -- linked against != Android framework APIs
      * _Example:_ <a href="http://code.google.com/android/add-ons/google-apis/maps-overview.html"> Google Maps library</a>

## Declare components

* _Example:_ manifest file / declare an activity

    ```
    <?xml version="1.0" encoding="utf-8"?>
    <manifest ... >
        <application android:icon="@drawable/app_icon.png" ... >
            <activity android:name="com.example.project.ExampleActivity"
                      android:label="@string/example_label" ... >
            </activity>
            ...
        </application>
    </manifest>
    ```

* see 
  * <a href="/guide/topics/manifest/application-element">&lt;application&gt;</a> element
  * <a href="/guide/topics/manifest/activity-element">&lt;activity&gt;</a> element
  * see [App manifest overview](guide.topics.manifest.manifest-intro.md)

* elements -- to declare -- ALL app components
  * <a href="/guide/topics/manifest/activity-element">&lt;activity&gt;</a>elements
    * for activities
  * <a href="/guide/topics/manifest/service-element">&lt;service&gt;</a>elements
    * for services
  * <a href="/guide/topics/manifest/receiver-element">&lt;receiver&gt;</a> elements
    * for broadcast receivers
  * <a href="/guide/topics/manifest/provider-element">&lt;provider&gt;</a> elements
    * for content providers

## Declare components capabilities
* TODO:

# App resources
* != app code /
  * let your app gracefully optimize its behavior | variety of device configurations
* TODO:

# Additional resources
* TODO:
