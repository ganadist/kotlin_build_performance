# Directory structure

* java : Project which contains java sources only
* kotlin : Project which contains kotlin sources only
* tools : Python script to generate source codes

# Build Performance Result

```
$ git clean -ffdx

$ ./gradlew :java:assemble --no-build-cache

> Task :java:processResources NO-SOURCE
> Task :java:compileJava
> Task :java:classes
> Task :java:jar
> Task :java:assemble

BUILD SUCCESSFUL in 2s
2 actionable tasks: 2 executed


$ ./gradlew :kotlin:assemble --no-build-cache
> Task :kotlin:checkKotlinGradlePluginConfigurationErrors
> Task :kotlin:processResources NO-SOURCE
> Task :kotlin:compileKotlin
> Task :kotlin:compileJava NO-SOURCE
> Task :kotlin:classes UP-TO-DATE
> Task :kotlin:jar
> Task :kotlin:assemble

BUILD SUCCESSFUL in 1m 20s
3 actionable tasks: 3 executed


$ ./gradlew :kotlin-k2:assemble --no-build-cache
> Task :kotlin-k2:checkKotlinGradlePluginConfigurationErrors SKIPPED
> Task :kotlin-k2:processResources NO-SOURCE
> Task :kotlin-k2:compileKotlin
> Task :kotlin-k2:compileJava NO-SOURCE
> Task :kotlin-k2:classes UP-TO-DATE
> Task :kotlin-k2:jar
> Task :kotlin-k2:assemble

BUILD SUCCESSFUL in 1m 1s
2 actionable tasks: 2 executed

```
