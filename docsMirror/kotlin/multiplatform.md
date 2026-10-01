# Kotlin Multiplatform  |  Android Developers

**Source:** [https://developer.android.com/kotlin/multiplatform](https://developer.android.com/kotlin/multiplatform)

---

Save and categorize content based on your preferences. 

![](https://developer.android.com/static/images/picto-icons/kmp.svg)

###  Kotlin Multiplatform 

Write a single codebase that runs on multiple platforms with Kotlin Multiplatform.

[Kotlin Multiplatform (KMP)](https://kotlinlang.org/multiplatform/) is officially supported by Google for sharing business logic between Android and iOS. Kotlin Multiplatform is [stable and production-ready](https://kotlinlang.org/docs/multiplatform/supported-platforms.html#current-platform-stability-levels-for-the-core-kotlin-multiplatform-technology). With JetBrains' [Compose Multiplatform (CMP)](https://www.jetbrains.com/compose-multiplatform/), developers can also share UI across platforms.

[ ![](https://developer.android.com/static/images/cluster-illustrations/play-webinar-16-9.svg) ](https://developer.android.com/courses/pathways/kotlin-multiplatform)

Pathway

###  [ Basics of Kotlin Multiplatform ](https://developer.android.com/courses/pathways/kotlin-multiplatform)

Start your journey into multi-platform development today. This pathway will guide you through the essentials of Kotlin Multiplatform, from setting up your project, sharing code, and using platform-specific APIs, to migrating the Room Database to Kotlin Multiplatform. 

[Learn & earn a badge](https://developer.android.com/courses/pathways/kotlin-multiplatform)

[ ![](https://developer.android.com/static/images/cluster-illustrations/android-development-kit-16-9.svg) ](https://plugins.jetbrains.com/plugin/14936-kotlin-multiplatform)

Android Studio Plugin

###  [ Kotlin Multiplatform Plugin ](https://plugins.jetbrains.com/plugin/14936-kotlin-multiplatform)

We recommend installing the Kotlin Multiplatform Android Studio Plugin developed by JetBrains to improve the development experience within Android Studio. 

  * **New project wizard** : Create a new multiplatform project within the IDE.
  * **Preflight checks** : Preflight checks help you configure your environment.
  * **Run configurations** : Run, debug, and test applications on both iOS and Android directly from the IDE.
  * **Basic Swift support in the IDE** : Get basic Swift support in the IDE, including cross-language debugging tools, navigation, and quick documentation.



[Go to JetBrains Marketplace](https://plugins.jetbrains.com/plugin/14936-kotlin-multiplatform)

check_circle 

###  Deduplicate code 

Your complex business logic doesn't have to be duplicated on each platform. 

check_circle 

###  No complete rewrite 

With Kotlin Multiplatform, you don't need to rewrite your whole application to start sharing code between platforms. 

check_circle 

###  Native performance 

Kotlin Multiplatform compiles into the native way the target platform runs code, delivering performance on par with native implementations. 

## Kotlin Multiplatform and Jetpack libraries

Many of our Jetpack libraries have already been migrated to be KMP-ready. The following Jetpack libraries provide KMP support:

![Android logo](/static/images/logos/android.svg) **Built by Android** ![JetBrains logo](/static/images/logos/jetbrains.svg) **Built by JetBrains** device_unknown **Not supported**

Library | Latest Release | Android | iOS | JVM | Web |  [ annotation ](/jetpack/androidx/releases/annotation) |  September 23, 2026   


  * [1.11.0](/jetpack/androidx/releases/annotation#1.11.0)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
---|---|---|---|---|---  
[ collection ](/jetpack/androidx/releases/collection) |  September 23, 2026   


  * [1.6.0](/jetpack/androidx/releases/collection#1.6.0)
  * [1.7.0-rc01](/jetpack/androidx/releases/collection#1.7.0-rc01)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
[ compose ](/jetpack/androidx/releases/compose-runtime) |  September 09, 2026   


  * [1.12.1](/jetpack/androidx/releases/compose-runtime#1.12.1)
  * [1.13.0-alpha03](/jetpack/androidx/releases/compose-runtime#1.13.0-alpha03)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg)  
[ datastore ](/jetpack/androidx/releases/datastore)   
  
[ article Documentation ](/kotlin/multiplatform/datastore) |  September 09, 2026   


  * [1.2.1](/jetpack/androidx/releases/datastore#1.2.1)
  * [1.3.0-alpha11](/jetpack/androidx/releases/datastore#1.3.0-alpha11)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
[ lifecycle ](/jetpack/androidx/releases/lifecycle)   
  
[ article Documentation ](https://kotlinlang.org/docs/multiplatform/compose-lifecycle.html) |  September 23, 2026   


  * [2.11.0](/jetpack/androidx/releases/lifecycle#2.11.0)
  * [2.12.0-alpha04](/jetpack/androidx/releases/lifecycle#2.12.0-alpha04)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
[ viewModel ](/jetpack/androidx/releases/lifecycle)   
  
[ article Documentation ](/kotlin/multiplatform/viewmodel) |  September 23, 2026   


  * [2.11.0](/jetpack/androidx/releases/lifecycle#2.11.0)
  * [2.12.0-alpha04](/jetpack/androidx/releases/lifecycle#2.12.0-alpha04)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
[ viewModel-compose ](/jetpack/androidx/releases/lifecycle)   
  
[ article Documentation ](https://kotlinlang.org/docs/multiplatform/compose-viewmodel.html) |  September 23, 2026   


  * [2.11.0](/jetpack/androidx/releases/lifecycle#2.11.0)
  * [2.12.0-alpha04](/jetpack/androidx/releases/lifecycle#2.12.0-alpha04)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg)  
[ navigation ](/jetpack/androidx/releases/navigation)   
  
[ article Documentation ](https://kotlinlang.org/docs/multiplatform/compose-navigation.html) |  September 23, 2026   


  * [2.10.2](/jetpack/androidx/releases/navigation#2.10.2)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg)  
[ navigation3 ](/jetpack/androidx/releases/navigation3) |  September 23, 2026   


  * [1.2.0](/jetpack/androidx/releases/navigation3#1.2.0)
  * [1.3.0-alpha01](/jetpack/androidx/releases/navigation3#1.3.0-alpha01)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg)  
[ navigationevent ](/jetpack/androidx/releases/navigationevent) |  September 23, 2026   


  * [1.1.2](/jetpack/androidx/releases/navigationevent#1.1.2)
  * [1.2.0-rc01](/jetpack/androidx/releases/navigationevent#1.2.0-rc01)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg) | ![](/static/images/logos/jetbrains.svg)  
[ paging ](/jetpack/androidx/releases/paging) |  August 12, 2026   


  * [3.5.1](/jetpack/androidx/releases/paging#3.5.1)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
[ room ](/jetpack/androidx/releases/room)   
  
[ article Documentation ](/kotlin/multiplatform/room) |  September 09, 2026   


  * [2.8.5](/jetpack/androidx/releases/room#2.8.5)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) |  device_unknown  
[ savedstate ](/jetpack/androidx/releases/savedstate) |  September 23, 2026   


  * [1.5.0](/jetpack/androidx/releases/savedstate#1.5.0)
  * [1.6.0-alpha04](/jetpack/androidx/releases/savedstate#1.6.0-alpha04)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
[ sqlite ](/jetpack/androidx/releases/sqlite)   
  
[ article Documentation ](/kotlin/multiplatform/sqlite) |  September 09, 2026   


  * [2.7.1](/jetpack/androidx/releases/sqlite#2.7.1)
  * [2.8.0-alpha01](/jetpack/androidx/releases/sqlite#2.8.0-alpha01)

| ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg) | ![](/static/images/logos/android.svg)  
  
If you have feedback on these libraries, share it through the [issue tracker](https://issuetracker.google.com/issues/new?component=1337890&template=1803002).

Libraries published by JetBrains wrap Android artifacts together with artifacts for other platforms so you can seamlessly consume any and all of them in your multiplatform projects. To learn about the underlying publishing process, see [How multiplatform Jetpack libraries are packaged](https://kotlinlang.org/docs/multiplatform/compose-multiplatform-jetpack-libraries.html).

###  [ KMP module wizard ](https://developer.android.com/kotlin/multiplatform/migrate)

You can start migrating to KMP by creating a KMP shared module within Android Studio. This module automatically applies all the necessary plugins, including the Android-KMP plugin, to start developing Android and iOS apps. 

[Add KMP to your project](https://developer.android.com/kotlin/multiplatform/migrate)

###  [ Live Edit for JetBrains' Compose Multiplatform ](https://developer.android.com/develop/ui/compose/tooling/iterative-development)

Live Edit works when building on Android Devices editing any code within the project, not just in `androidMain`. 

[Learn more](https://developer.android.com/develop/ui/compose/tooling/iterative-development)

###  [ Previews for JetBrains' Compose Multiplatform ](https://developer.android.com/develop/ui/compose/tooling/previews)

Previews for Jetpack Compose are also available for JetBrains' Compose Multiplatform from the `commonMain` source set. 

[Learn more](https://developer.android.com/develop/ui/compose/tooling/previews)

![](https://developer.android.com/static/images/kotlin/kmp-apps/blinkit.png)

Blinkit 

![](https://developer.android.com/static/images/kotlin/kmp-apps/cash-app.svg)

Cash App 

![](https://developer.android.com/static/images/kotlin/kmp-apps/duolingo.svg)

Duolingo 

![](https://developer.android.com/static/images/kotlin/kmp-apps/forbes.png)

Forbes 

![](https://developer.android.com/static/images/kotlin/kmp-apps/google-docs.svg)

Google Docs 

![](https://developer.android.com/static/images/kotlin/kmp-apps/jiohotstar.png)

JioHotstar 

![](https://developer.android.com/static/images/kotlin/kmp-apps/stone.svg)

Stone

![](https://developer.android.com/static/images/kotlin/kmp-apps/swiggy.svg)

Swiggy 

![](https://developer.android.com/static/images/kotlin/kmp-apps/ultrahuman.svg)

Ultrahuman 

![](https://developer.android.com/static/images/kotlin/kmp-apps/wrike.svg)

Wrike 

![](https://developer.android.com/static/images/kotlin/kmp-apps/zomato.png)

Zomato 

looks_one 

###  Tier 1 

Code is fully tested in CI; including both host-side and on-device tests. We're tracking source and binary compatibility in accordance with our [semantic versioning policies](/jetpack/androidx/versions). 

  * **Android**
  * **JVM**
  * **iOS**



looks_two 

###  Tier 2 

Code is partially tested on CI; limited to host-side tests. We don't track source or binary compatibility. 

  * **macOS**
  * **Linux**



looks_3 

###  Tier 3 

Code is untested on CI. No source or binary compatibility tracking. 

  * **watchOS**
  * **tvOS**
  * **Windows**
  * **JavaScript**
  * **WASM**



[ ![](https://developer.android.com/static/images/picto-icons/layout.svg) ](https://github.com/android/kotlin-multiplatform-samples)

###  [ Kotlin Multiplatform samples ](https://github.com/android/kotlin-multiplatform-samples)

A set of Kotlin Multiplatform samples that demonstrate how to use the Jetpack libraries for Android and iOS. 

[Sample](https://github.com/android/kotlin-multiplatform-samples)

[ ![](https://developer.android.com/static/images/picto-icons/theming.svg) ](https://developer.android.com/codelabs/kmp-get-started)

###  [ Get started with Kotlin Multiplatform ](https://developer.android.com/codelabs/kmp-get-started)

Guided onboarding on how to add KMP to your project. 

[Codelab](https://developer.android.com/codelabs/kmp-get-started)

[ ![](https://developer.android.com/static/images/picto-icons/graph-line.svg) ](https://developer.android.com/codelabs/kmp-migrate-room)

###  [ Migrate Room to Kotlin Multiplatform ](https://developer.android.com/codelabs/kmp-migrate-room)

Guided migration of Android-only Room to KMP. 

[Codelab](https://developer.android.com/codelabs/kmp-migrate-room)

[ ![](https://developer.android.com/static/images/picto-icons/kmp.svg) ](https://kotlinlang.org/docs/multiplatform/get-started.html)

###  [ In-depth Guidance ](https://kotlinlang.org/docs/multiplatform/get-started.html)

More in-depth guidance is available in Kotlin Multiplatform documentation hub on Kotlinlang.org. 

[Documentation](https://kotlinlang.org/docs/multiplatform/get-started.html)

Learn what Kotlin Multiplatform is, how it works, and the benefits of using it. 

[Video](https://www.youtube.com/watch?v=gP5Y-ct6QXI)

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
