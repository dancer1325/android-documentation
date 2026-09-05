https://developer.android.com/develop/ui/compose/designsystems/material3

* goal
  * how to implement Material -- with -- Compose's implementation of [Material Design 3](https://m3.material.io/)

* Material3
  * == theming + components + features to customize
    * features to customize
      * dynamic color
      * typography
      * ...
    * theming allowed
      * [color scheme](https://m3.material.io/styles/color/system/overview)
        * TODO:
      * [typography](https://m3.material.io/styles/typography/overview)
        * TODO:
      * [shapes](https://m3.material.io/styles/shape/overview)
        * TODO:
  * others naming
    * "Material Design 3", "M3"
  * see [Reply sample app](https://github.com/dancer1325/android-jetpackcompose-samples/tree/main/Reply)
  * steps to use 
    * add | "build.gradle"
    
    `implementation "androidx.compose.material3:material3:$material3_version"`
  * if you want to use experimental features -> 
    `import androidx.compose.material3.ExperimentalMaterial3Api`
  * `androidx.compose.material3.MaterialTheme`
    * 👀way that Jetpack Compose implements it👀
  * TODO:
