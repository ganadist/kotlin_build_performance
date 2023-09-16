import org.gradle.api.tasks.compile.JavaCompile
import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.jetbrains.kotlin.gradle.tasks.KotlinJvmCompile

buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.9.10")
    }
}

val JVM_TARGET = "11"

subprojects {
    tasks
        .withType<JavaCompile>()
        .configureEach {
            sourceCompatibility = JVM_TARGET
            targetCompatibility = JVM_TARGET
        }

    tasks
        .withType<KotlinJvmCompile>()
        .configureEach {
            compilerOptions {
                jvmTarget.set(JvmTarget.fromTarget(JVM_TARGET))
            }
        }
}

