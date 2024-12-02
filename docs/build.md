https://developer.android.com/build

* Android build system
  * app resources & source code -- are
    * compiled
    * packaged | APKs or Android App Bundles
      * uses
        * test,
        * deploy,
        * sign,
        * distribute

# Android build glossary
* build aspects / configured -- thanks to -- Gradle & Android Gradle plugin
  * Build types
    * == properties /
      * used by Gradle to
        * build the app
        * package the app 
    * configured / development lifecycle's stages 
      * _Example1:_  debug build type
        * enables debug options
        * signs the app -- via the -- debug key
        * created by default, by Android Studio
      * _Example2:_ release build type can 
        * shrink,
        * obfuscate,
        * sign -- via the -- release key
        * created by default, by Android Studio
    * requirements
      * \>=1 build type -- to build -- your app
  * Product flavors
    * == different versions of your app / can be set | production
      * optional
      * _Example:_ free & paid versions
  * Build variants
    * == cross-product of build type & product flavor 
      * if you configure the build types & product flavors -> configure INDIRECTLY build variants
      * if you create additional build types OR product flavors -> creates additional build variants 
    * uses
      * by Gradle, -- to build your -- app
        * _Example:_ build the debug version of your product flavors
  * TODO:


* TODO:

# Java versions in Android builds
* TODO:

# Build configuration files
* TODO:

# Version catalogs
* TODO:

# Other build systems
* [Bazel](https://bazel.build/)
  * possible
  * NOT officially supported
    * NOR -- supported by -- Android Studio
  * [Bazel limitations](https://github.com/bazelbuild/bazel/issues?q=is%3Aissue+is%3Aopen+label%3Ateam-Android) 

  
