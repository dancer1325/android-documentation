https://developer.android.com/build/android-build-structure

* Android projects
  * == many build-related files / directory structures -- organize -- your application source & resources
    * build-related files -- MUST be writing, following a -- [declarative approach](https://blog.gradle.org/declarative-gradle)
      * 👀== build logic & task definitions ONLY | plugins 👀
        * -> build files == data declarations 
  * 's structure
    * `build.gradle(.kts)`
      * ONLY contain plugin declarations
    * `local.properties`
      * local machine configuration
        * == properties -- related to the -- local machine
        * _Example:_ location of the Android SDK
        * exclude -- from -- source control!
    * `app/`
      * [subproject directory](https://docs.gradle.org/current/userguide/intro_multi_project_builds.html)
      * uses
        * applications
        * libraries
      * conventional name, BUT can be changed
      * `src/main/`
        * MAIN source set
        * `java/` or `kotlin/`
          * java or kotlin source code
          * `java/` can contain Java & Kotlin source code
          * if project ONLY contains Kotlin source code -> name `kotlin/`
          * Android is kotlin-first
            * Reason: 🧠new APIs target Kotlin 🧠
            * ALTHOUGH, Java ALSO supported
        * `res/`
          * == [Android resources files](guide.topics.resources.providing-resources.md)
        * [`AndroidManifest.xml`](guide.topics.manifest.manifest-intro.md)
