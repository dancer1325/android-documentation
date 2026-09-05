https://developer.android.com/develop/ui/compose/state

* goal
  * how to set & use state | Compose app
    * connection between state -- & -- composables
  * state APIs / -- provided by -- Jetpack Compose

* app's state
  * 👀== ANY value / can change | time 👀
    * == broad definition / can encompass EVERYTHING -- [Room database, variable | class] --
  * -- is displayed state to the -- user
    * _Example:_
      * Snackbar / shows | network connection NOT established
      * blog post & associated comments
      * Ripple animations | buttons / play | user clicks them
      * Stickers / user can draw | top of an image
  * Jetpack Compose 
    * helps be explicit about Android app's state
      * where to store
        * -- via -- `remember` API either mutable or immutable objects
          * ways to declare `MutableState` objects
            * `val mutableState = remember { mutableStateOf(default) }`
            * `var value by remember { mutableStateOf(default) }`
              * requirements
              
                ```
                import androidx.compose.runtime.getValue
                import androidx.compose.runtime.setValue
                ``

            * `val (value, setValue) = remember { mutableStateOf(default) }`
          * _Example:_ `StateOverviewSnippets.kt`
      * how to use 

* State & Composition
  * [recomposition | Compose](develop.ui.compose.mental-model.md)
    * == call the SAME composable / NEW arguments
      * 👀these arguments == UI state 👀
        * -> update a state == recomposition takes place
      * _Example:_ `StateOverviewSnippets.kt`

* OTHER supported types of state
  * TODO:

* https://www.youtube.com/watch?v=mymWGMy9pYI
  * TODO: