# OTA images for Google Pixel  |  Android Developers

**Source:** [https://developer.android.com/about/versions/17/qpr1/download-ota](https://developer.android.com/about/versions/17/qpr1/download-ota)

---

#  OTA images for Google Pixel Save and categorize content based on your preferences. 

Applying an OTA image can help you recover a device that received an OTA update for an Android 17 Beta build but wouldn't start up after the update was installed. If you are trying to get Android 17 on your device but you aren't trying to recover from a failed OTA update, see [Get Android 17](/about/versions/17/get) instead.

Building on the [initial release of Android 17](/about/versions/17), we continue to update the platform with fixes and improvements that are then rolled out to supported devices. These releases happen on a quarterly cadence through _Quarterly Platform Releases_ (QPRs), which are delivered both to AOSP and to Google Pixel devices as part of _Feature Drops_. 

Although these updates don't include app-impacting API changes, we provide images of the latest QPR beta builds so you can test your app with these builds as needed (for example, if there are upcoming features that might impact the user experience of your app).

To find OTA images for already-released, stable versions of the platform, see [Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).

Applying an OTA image can help you recover a device that received an OTA update for an Android 17 QPR beta build but wouldn't start up after the update was installed. If you are trying to get Android 17 QPR1 on your device but you aren't trying to recover from a failed OTA update, see [Get Android 17 QPR beta builds](/about/versions/17/get-qpr) instead. 

OTA images are available for the following Pixel devices:

  * Pixel 6
  * Pixel 6 Pro
  * Pixel 6a
  * Pixel 7
  * Pixel 7 Pro
  * Pixel 7a
  * Pixel Tablet
  * Pixel Fold
  * Pixel 8
  * Pixel 8 Pro
  * Pixel 8a
  * Pixel 9
  * Pixel 9 Pro
  * Pixel 9 Pro XL
  * Pixel 9 Pro Fold
  * Pixel 9a
  * Pixel 10
  * Pixel 10 Pro
  * Pixel 10 Pro XL
  * Pixel 10 Pro Fold
  * Pixel 10a

After you've installed a beta build to your Pixel device, your device is automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) and offered continuous over-the-air (OTA) updates to the latest beta builds (including QPRs) until you choose to unenroll that device from the program. 

We also deliver flashable images at each milestone, so you can choose the approach that works best for your test environment.

Use the following links and instructions to update your supported device to the latest build. See [Get Android 17](/about/versions/17/get) for other ways to get Android 17 for testing and development.

## Apply an OTA image

![](/static/images/lockups/android-stacked.svg)

Download an OTA device image from the following table and apply it by following the [updating instructions](https://developers.google.com/android/ota#instructions) listed on [Full OTA Images for Nexus and Pixel Devices](https://developers.google.com/android/ota).

You can choose to return to the latest public build at any time.

**Warning:** Before applying an Android 17 OTA image, we strongly recommend that you [unlock the bootloader](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) on your device if possible. Unlocking the bootloader requires a full device reset that removes all user data on the device, so make sure to back up your data first.

### Device OTA Images

**Release date** | August 17, 2026  
---|---  
**Builds** | CP31.260623.012  
**Emulator support** | x86 (64-bit), ARM (v8-A)  
**Security patch level** | 2026-07-05  
**Google Play services** | 26.22.36  
Device | Download Link and SHA-256 Checksum  
---|---  
Pixel 6 |  oriole_beta-ota-cp31.260623.012-d86b1d26.zip   
`d86b1d26e04356f5298fc365ac787b688f6a13c9075e1f582a10ada739e45482`  
Pixel 6 Pro |  raven_beta-ota-cp31.260623.012-e56a3679.zip   
`e56a3679d4cdb7b48b19db90d1e40fad0e4bcee652ef82abde6e0fa548662ec4`  
Pixel 6a |  bluejay_beta-ota-cp31.260623.012-25293397.zip   
`2529339786aab5615de4334647568ee55d239d0d8f0fbf636a8b52f286f5f81c`  
Pixel 7 |  panther_beta-ota-cp31.260623.012-20d75b9e.zip   
`20d75b9e22f5d1a981cd5185f2e72f8bb1dff10c616013f96acdb7309c55c518`  
Pixel 7 Pro |  cheetah_beta-ota-cp31.260623.012-e83bdb84.zip   
`e83bdb84f096dafb6e01faddea602a1406c8c56c3f304b1d21108aeb0d2b95f0`  
Pixel 7a |  lynx_beta-ota-cp31.260623.012-bc765f01.zip   
`bc765f012ae68d5959872c17b48c2e080139db7defd4aa51f7509799a46d7750`  
Pixel Fold |  felix_beta-ota-cp31.260623.012-274c71fd.zip   
`274c71fd5ea67584c173edfa587597d5cb0841cb002e1feae4baa2b9faa9795a`  
Pixel Tablet |  tangorpro_beta-ota-cp31.260623.012-a8840430.zip   
`a8840430dc6e46f8035438be8e8b4c29ff76119ab05496abf33e5f5b7135a22d`  
Pixel 8 |  shiba_beta-ota-cp31.260623.012-d54a5b70.zip   
`d54a5b70ce1736dd76765164fe735724704b09c4363b43068347c132fdc40a4d`  
Pixel 8 Pro |  husky_beta-ota-cp31.260623.012-551688e6.zip   
`551688e63e2576fede5e78597f070d0fe63cd4e6f59ebd6e22b33e2ebddf063b`  
Pixel 8a |  akita_beta-ota-cp31.260623.012-92f88b59.zip   
`92f88b59e2ee714a2916b1b6764e5904a3ab96849ed86311b69cf223a2e1f8c5`  
Pixel 9 |  tokay_beta-ota-cp31.260623.012-bdcf971e.zip   
`bdcf971ef4fe62867a372f4efbae897ae6441615d754d84bde0821132afa6d32`  
Pixel 9 Pro |  caiman_beta-ota-cp31.260623.012-d7c20aa6.zip   
`d7c20aa658a5923fe26353266f6000980533ae5ea70c34b7ea94d889fbd986a9`  
Pixel 9 Pro XL |  komodo_beta-ota-cp31.260623.012-87e00d3a.zip   
`87e00d3a76e77b911815049f8bb337f8ab8d9ccd8ea41c8a25eb1d2e6da38f40`  
Pixel 9 Pro Fold |  comet_beta-ota-cp31.260623.012-b89ca289.zip   
`b89ca289dd4c52c4accad9c228e766854f9814446000357f02890897d2a73051`  
Pixel 9a |  tegu_beta-ota-cp31.260623.012-29f2ec9d.zip   
`29f2ec9da17a23c74a90229cdfc904b418fbbe6565dbd0fc5dcaaaeeb7394ab9`  
Pixel 10 |  frankel_beta-ota-cp31.260623.012-2263efcf.zip   
`2263efcffd574d38ecb52bab646bb909a34974e039b9bd4c3daeb29aae239b9a`  
Pixel 10 Pro |  blazer_beta-ota-cp31.260623.012-9fef009a.zip   
`9fef009a28acc2be0f91e2016e3c4b9acaf232cf5f48aa5dad7c5daa0c51d154`  
Pixel 10 Pro XL |  mustang_beta-ota-cp31.260623.012-ebcfa9df.zip   
`ebcfa9dfd68101577078f9bed07abc75d48718ff57437b182d4c4ab6aee52cf8`  
Pixel 10 Pro Fold |  rango_beta-ota-cp31.260623.012-044cfeb7.zip   
`044cfeb7355ce5ed1c4eb071b6200ce8d1d06d11e5a5185d8e73508ae770dc09`  
Pixel 10a |  stallion_beta-ota-cp31.260623.012-e33219f6.zip   
`e33219f6d5a582d53f94c9d216bfc1a4a72d620cfc9b8529c400cc1d4db80e30`  
  
## Return to a public build

You can either use the Android Flash Tool to [flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images) page and then manually flash it to the device.

**Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/oriole_beta-ota-cp31.260623.012-d86b1d26.zip)

_oriole_beta-ota-cp31.260623.012-d86b1d26.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/raven_beta-ota-cp31.260623.012-e56a3679.zip)

_raven_beta-ota-cp31.260623.012-e56a3679.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/bluejay_beta-ota-cp31.260623.012-25293397.zip)

_bluejay_beta-ota-cp31.260623.012-25293397.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/panther_beta-ota-cp31.260623.012-20d75b9e.zip)

_panther_beta-ota-cp31.260623.012-20d75b9e.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/cheetah_beta-ota-cp31.260623.012-e83bdb84.zip)

_cheetah_beta-ota-cp31.260623.012-e83bdb84.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/lynx_beta-ota-cp31.260623.012-bc765f01.zip)

_lynx_beta-ota-cp31.260623.012-bc765f01.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/felix_beta-ota-cp31.260623.012-274c71fd.zip)

_felix_beta-ota-cp31.260623.012-274c71fd.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/tangorpro_beta-ota-cp31.260623.012-a8840430.zip)

_tangorpro_beta-ota-cp31.260623.012-a8840430.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/shiba_beta-ota-cp31.260623.012-d54a5b70.zip)

_shiba_beta-ota-cp31.260623.012-d54a5b70.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/husky_beta-ota-cp31.260623.012-551688e6.zip)

_husky_beta-ota-cp31.260623.012-551688e6.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/akita_beta-ota-cp31.260623.012-92f88b59.zip)

_akita_beta-ota-cp31.260623.012-92f88b59.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/tokay_beta-ota-cp31.260623.012-bdcf971e.zip)

_tokay_beta-ota-cp31.260623.012-bdcf971e.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/caiman_beta-ota-cp31.260623.012-d7c20aa6.zip)

_caiman_beta-ota-cp31.260623.012-d7c20aa6.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/komodo_beta-ota-cp31.260623.012-87e00d3a.zip)

_komodo_beta-ota-cp31.260623.012-87e00d3a.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/comet_beta-ota-cp31.260623.012-b89ca289.zip)

_comet_beta-ota-cp31.260623.012-b89ca289.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/tegu_beta-ota-cp31.260623.012-29f2ec9d.zip)

_tegu_beta-ota-cp31.260623.012-29f2ec9d.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/frankel_beta-ota-cp31.260623.012-2263efcf.zip)

_frankel_beta-ota-cp31.260623.012-2263efcf.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/blazer_beta-ota-cp31.260623.012-9fef009a.zip)

_blazer_beta-ota-cp31.260623.012-9fef009a.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/mustang_beta-ota-cp31.260623.012-ebcfa9df.zip)

_mustang_beta-ota-cp31.260623.012-ebcfa9df.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/rango_beta-ota-cp31.260623.012-044cfeb7.zip)

_rango_beta-ota-cp31.260623.012-044cfeb7.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/stallion_beta-ota-cp31.260623.012-e33219f6.zip)

_stallion_beta-ota-cp31.260623.012-e33219f6.zip_

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-16 UTC."],[],[]] 
