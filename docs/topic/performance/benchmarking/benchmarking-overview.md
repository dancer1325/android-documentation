# Benchmark your app  |  App quality  |  Android Developers

**Source:** [https://developer.android.com/topic/performance/benchmarking/benchmarking-overview](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview)

---

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Benchmark your app Stay organized with collections  Save and categorize content based on your preferences. 

Benchmarking is a way to inspect and monitor the performance of your app. You can regularly run benchmarks to analyze and debug performance problems and help ensure that you don't introduce regressions in recent changes.

Android offers two benchmarking libraries and approaches for analyzing and testing different kinds of situations in your app: Macrobenchmark and Microbenchmark.

## Macrobenchmark

The [Macrobenchmark](/studio/profile/macrobenchmark) library measures larger end-user interactions, such as startup, interacting with the UI, and animations. The library provides direct control over the performance environment you're testing. It lets you control compiling and lets you start and stop your app to directly measure actual app startup or scrolling.

The Macrobenchmark library injects events and monitors results externally from a test app that is built with your tests. Therefore, when writing the benchmarks, you don't call your app code directly and instead navigate within your app as a user.

## Microbenchmark

The [Microbenchmark](/studio/profile/benchmark) library lets you benchmark app code directly in a loop. This is designed for measuring CPU work that assesses best-case performance—such as warmed up Just in Time (JIT) and disk accesses cached—that you might see with an inner-loop or a specific hot function. The library can only measure the code that you can call directly in isolation.

These are good cases for benchmarking: * When your app needs to process a complex data structure. * When your app has a specific computation-heavy algorithm that it calls multiple times during the app run.

You can also measure parts of your UI. For example, you can measure the cost of `RecyclerView` item binding, how long it takes to inflate a layout, or the performance of the layout-and-measure pass of your `View` class.

However, you can't measure how the benchmarked cases contribute to the overall user experience. In some scenarios, benchmarking doesn't tell you if you're improving a bottleneck like dropped frames or app startup time. For this reason, it's crucial to identify those bottlenecks first with the [Android Profiler](/studio/profile). After you find the code you want to investigate and optimize, the benchmarked loop can run repeatedly to create less noisy results. This lets you focus on one area of improvement.

The Microbenchmark library only reports information about your app, not about the system overall. Therefore, it's best at analyzing performance of situations specific to the app, not ones that might relate to overall system issues.

## Benchmark library comparison

| Macrobenchmark | Microbenchmark  
---|---|---  
Function  | Measure high-level entry points or interactions, such as activity launch or scrolling a list. | Measure individual functions.   
Scope  | Out-of-process test of full app. | In-process test of CPU work.   
Speed  | Medium iteration speed. It can exceed a minute. | Fast iteration speed. Often less than 10 seconds.  
Tracing  | Results come with system traces.  | Results come with a minimal system trace and a method trace by default.  
  
## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Create Baseline Profiles {:#creating-profile-rules}](/topic/performance/baselineprofiles/create-baselineprofile)
  * [JankStats Library](/topic/performance/jankstats)
  * [Overview of measuring app performance](/topic/performance/measuring-performance)



Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-11 UTC."],[],[]] 
