https://developer.android.com/training/basics/intents

* goal
  * how to use an Intent -- to perform -- some basic interactions with other apps
    * _Example:_ starting another app, receiving a result from that app, making your app able to respond to intents from other apps

* intent
  * == message -- defined by an -- `Intent` object

* `Intent`
  * == 👀your app's "intent" -- to do -- something 👀
    * _Example:_ your app -- start an -- activity / contained | separate app 
    * == action to perform + data to be acted on + component's category + other instructions
  * 👀uses👀
    * activate
      * App activities,
      * services,
      * broadcast receivers
  * way to pass an `Intent` -- to the -- system
    * `startActivity()`
      * the system -- thanks to the `Intent` --
        * identify the appropriate app component / -- based on -- intent filters
          * if there are SEVERAL apps -> user can select which one to use
        * start the appropriate app component / -- passes the -- `Intent`
          * == instance of appropriate app component
  * types
    * explicit
      * _Example:_ start a specific Activity instance
    * implicit
      * _Example:_ start any component / -- can handle the -- intended action ("capture a photo")
  * use case
    * Android app typically has SEVERAL activities /
      * EACH activity -- displays a -- UI / user -- can perform a -- specific task (_Example:_ viewing a map or taking a photo)
        * if you want that the user can navigate from one activity -- to -- another activity -> your app MUST use an `[Intent](https://developer.android.com/reference/android/content/Intent)`

* Intent filters
  * `<intent-filter>`
  * possible to have ANY number of Intent filters / app component
    * EACH Intent filter -- describe a -- DIFFERENT capability of that component
