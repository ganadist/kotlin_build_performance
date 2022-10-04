# Directory structure

* java : Project which contains java sources only
* kotlin : Project which contains kotlin sources only
* tools : Python script to generate source codes

# Build Performance Result

```
$ ./gradlew clean

> Task :clean
> Task :java:clean
> Task :kotlin:clean

BUILD SUCCESSFUL in 481ms
3 actionable tasks: 3 executed


$ ./gradlew :java:assemble

> Task :java:compileJava
> Task :java:processResources NO-SOURCE
> Task :java:classes
> Task :java:jar
> Task :java:assemble

BUILD SUCCESSFUL in 3s
2 actionable tasks: 2 executed


$ ./gradlew :kotlin:assemble

> Task :kotlin:processResources NO-SOURCE
> Task :kotlin:compileKotlin
> Task :kotlin:compileJava NO-SOURCE
> Task :kotlin:classes UP-TO-DATE
> Task :kotlin:jar
> Task :kotlin:inspectClassesForKotlinIC
> Task :kotlin:assemble

BUILD SUCCESSFUL in 1m 22s
3 actionable tasks: 3 executed

$ ./gradlew :kotlin-k2:assemble

> Task :kotlin-k2:processResources NO-SOURCE
> Task :kotlin-k2:compileKotlin
w: ATTENTION!
 This build uses experimental K2 compiler: 
  -Xuse-k2

> Task :kotlin-k2:compileJava NO-SOURCE
> Task :kotlin-k2:classes UP-TO-DATE
> Task :kotlin-k2:jar
> Task :kotlin-k2:inspectClassesForKotlinIC
> Task :kotlin-k2:assemble

BUILD SUCCESSFUL in 1m 1s
3 actionable tasks: 3 executed

```
