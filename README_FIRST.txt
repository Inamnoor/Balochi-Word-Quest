BALOCHI WORD QUEST — ANDROID TEST BUILD PROJECT

This project is an Android/Kivy adaptation of the Tkinter game you supplied.
It is not the original Tkinter program; Android requires a mobile-compatible UI.
The original word lists and token rules were retained. The interface keeps the
same branding, color palette, home/lesson/game flow, lives, score, streak,
hints, themes, and available sounds, adapted for a portrait phone screen.

IMPORTANT SOUND NOTE
The ZIP supplied these files:
  background.mp3, background1.mp3, button.mp3, correct.mp3, hint.mp3,
  win.mp3, wrong.mp3
The code also refers to lose.mp3, new_word.mp3, and skip.mp3, but those were
not supplied. The app safely continues without missing effects. background.mp3
is used for looping music when supported by the Android audio backend.

HOW TO GET THE APK WITHOUT INSTALLING BUILD TOOLS ON YOUR LAPTOP
This project includes a GitHub Actions workflow to build the APK in GitHub's
cloud runner. You will need a free GitHub account and internet access.

1. Create a NEW PUBLIC GitHub repository (public repos can use GitHub Actions
   without consuming the private-repository included minutes allowance).
2. Upload the CONTENTS of this folder to the repository, keeping the path:
      .github/workflows/build-android.yml
   Make sure the hidden .github folder is included.
3. Open the repository's Actions tab.
4. Select "Build Balochi Word Quest Android APK" and click "Run workflow".
5. Wait for the workflow to finish successfully.
6. Open the completed run and download the artifact named
   "balochi-word-quest-debug-apk". Extract it to get the .apk file.
7. Transfer the APK to your Android phone and open it. If prompted, allow your
   file manager to install apps from this source. Only install APKs you built
   from a project you trust.

If the build fails, download or copy the failed step's log and share it so it
can be fixed. First Android builds can take a while while the SDK/NDK downloads.

This is a debug/testing APK, not a Play Store release. The current game is an
initial mobile port and should be tested on your device before relying on it.
