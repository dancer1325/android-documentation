# Record Java/Kotlin methods  |  Android Studio  |  Android Developers

**Source:** [https://developer.android.com/studio/profile/record-java-kotlin-methods](https://developer.android.com/studio/profile/record-java-kotlin-methods)

---

#  Record Java/Kotlin methods Save and categorize content based on your preferences. 

Recording the Java/Kotlin methods called during your app's code execution lets you see the callstack and CPU usage at a given time. This data is useful for identifying sections of code that take a long time or a lot of system resources to execute. If you want a full view of the callstack including native call frames, use the [callstack sample](/studio/profile/sample-callstack) profiling task.

When recording Java or Kotlin methods, the Android Studio Profiler uses runtime instrumentation to inject timestamps at the entry and exit points of each method call. The profiler then aggregates and analyzes these timestamps to generate precise method tracing data and execution timings. Use method recording when you need exact visibility into specific method invocations. We recommend limiting recordings to five seconds or less to avoid performance overhead from runtime instrumentation.

**Note:** The timing information from tracing might deviate from production due to the overhead introduced by the instrumentation itself.

## Java/Kotlin methods overview

After you [run the **Find CPU Hotspots** task](/studio/profile#start-profiling) the Android Studio Profiler provides the following information:

![](/static/studio/images/profiler-jk-methods-recording.png)

  * **CPU Usage** : Shows CPU usage of your app as a percentage of total available CPU capacity by time. Note that the CPU usage includes not only Java/Kotlin methods but also native code. Highlight a section of the timeline to filter to the details for that time period.
  * **Interactions** : Shows user interaction and app lifecycle events along a timeline.
  * **Threads** : Shows the threads that your app runs on. In most cases, you'll want to first focus on the topmost thread that represents your app.



To identify the methods or call stacks that take the most time, use the [flame chart](/studio/profile/chart-glossary/flame-chart) or [top down](/studio/profile/chart-glossary/top-bottom-charts) chart.

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
