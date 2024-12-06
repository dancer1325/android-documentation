https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/compose-in-views

* goal
  * 👀| EXISTING app / View-based design, you cand add Compose-based UI👀

* steps to create a NEW Compose-based screen
  * your activity call `setContent()` / pass a composable function
    * -> add `androidx.activity:activity-compose:$latestVersion` dependency | "build.gradle"

* TODO: