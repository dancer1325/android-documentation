https://developer.android.com/develop/ui/compose/side-effects

* goal
  * BEST ways -- to manage -- side-effects
  * side-effect APIs Jetpack Compose

* side-effect
  * 👀:= change to the app's state / happens outside the scope of a composable function👀
    * ANY change / visible | rest of your app
  * 💡composables should IDEALLY be side-effect FREE 💡
    * Reason: 🧠due to composables'
      * lifecycle
      * properties -- _Example:_ unpredictable recompositions, execute recompositions of composables | different orders, or recompositions / can be discarded -- 🧠
    * use cases / are necessary
      * _Example:_ trigger a one-off event such as showing a snackbar, if certain state condition -> navigate to another screen 
      * recommendations
        * 👀call the actions -- from a -- controlled environment / -- aware of the -- composable's lifecycle 👀 

# State & effect use cases
* TODO:
      
