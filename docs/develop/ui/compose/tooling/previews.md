https://developer.android.com/develop/ui/compose/tooling/previews

* Android Wear
  * 👀!= Android👀
    * -> specific preview annotations
      * _Example:_ `@WearPreviewDevices`, `@WearPreviewFontScales`

* `@Preview`
  * vs run the app | emulator
    * save memory
  * 👀if you add SEVERAL ones | SAME function -> preview a composable / DIFFERENT properties👀 
    * recommendation
      * use [Gallery Mode](https://www.geeksforgeeks.org/galleryview-in-android-with-example/)
  * Dimensions
    * chosen automatically / wrap its content
      * if you want to define -> use `widthDp` & `heightDp` properties
        * _Example:_ `@Preview(widthDp = 50, heightDp = 50)`
  * Dynamic color preview
    * TODO: