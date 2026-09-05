# OTA images for Google Pixel  |  Android Developers

**Source:** [https://developer.android.com/about/versions/17/qpr1/download-ota](https://developer.android.com/about/versions/17/qpr1/download-ota)

---

  * [ Android Developers ](https://developer.android.com/)
  * [ Essentials ](https://developer.android.com/get-started)
  * [ Releases ](https://developer.android.com/about/versions)



#  OTA images for Google Pixel Stay organized with collections  Save and categorize content based on your preferences. 

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

**Release date** | July 1, 2026  
---|---  
**Builds** | CP31.260618.005  
**Emulator support** | x86 (64-bit), ARM (v8-A)  
**Security patch level** | 2026-06-05  
**Google Play services** | 26.20.31  
Device | Download Link and SHA-256 Checksum  
---|---  
Pixel 6 |  oriole_beta-ota-cp31.260618.005-9485881d.zip   
`9485881dd953d8ae92f3c70b04af0e2abe02d6ee70749e9e01b21b33fcf74769`  
Pixel 6 Pro |  raven_beta-ota-cp31.260618.005-5bf3392a.zip   
`5bf3392aad81c599441e2de33906c33aa0aeb1d2e5fdd47f95a0940c311c6acb`  
Pixel 6a |  bluejay_beta-ota-cp31.260618.005-d3320dd0.zip   
`d3320dd0ac71c3b21f2eb942c0172b44fcb1a46ed2ae7316fa604115a1f1ac36`  
Pixel 7 |  panther_beta-ota-cp31.260618.005-4bc68bd7.zip   
`4bc68bd71c46ba8033461bec00324333733fd57c62ed808002ebcce5774403de`  
Pixel 7 Pro |  cheetah_beta-ota-cp31.260618.005-99506ed1.zip   
`99506ed15401ba3d6aadd7cf8692c240011770eb2d788648d733ee3122533b9a`  
Pixel 7a |  lynx_beta-ota-cp31.260618.005-656e629a.zip   
`656e629a305be36cea1656ab36a976ee928af943143d16263461460e88399b9d`  
Pixel Fold |  felix_beta-ota-cp31.260618.005-3b0fc11c.zip   
`3b0fc11c7a5c168a3e7a7cd565a62f53b698a8053d99ec97516106e7ae7d1b25`  
Pixel Tablet |  tangorpro_beta-ota-cp31.260618.005-4a2c6f2c.zip   
`4a2c6f2ce1d5063a3286f7a541c9e8cf385aab877c7000dc839410cd473a51b9`  
Pixel 8 |  shiba_beta-ota-cp31.260618.005-8514ac60.zip   
`8514ac60d91bfa1e971f2271bcac244041a03ecf2872156cfb11b6af32c32fa6`  
Pixel 8 Pro |  husky_beta-ota-cp31.260618.005-8dcacb35.zip   
`8dcacb351deee9c415db8a7b8f1c15a2ae26e04383d2a46928884ce1670d8d51`  
Pixel 8a |  akita_beta-ota-cp31.260618.005-0527f1ac.zip   
`0527f1ac33de1c24562e3f971d6f9683d0b8c147c88484c8b56d2129dfbf6302`  
Pixel 9 |  tokay_beta-ota-cp31.260618.005-8ab19d74.zip   
`8ab19d74960736623df68281e377265467cabfaf516eca38acf6eb994d3fb8f4`  
Pixel 9 Pro |  caiman_beta-ota-cp31.260618.005-f071a5d0.zip   
`f071a5d0eea12fb56ce470427839fdfccdb38443548a90eba603948b0fec89e7`  
Pixel 9 Pro XL |  komodo_beta-ota-cp31.260618.005-52cc903a.zip   
`52cc903a90b7e4bc1bae65ef67d43df59bdd90b8a5f1e664c2c34e99862671f4`  
Pixel 9 Pro Fold |  comet_beta-ota-cp31.260618.005-29df0d9f.zip   
`29df0d9f7f7068020395175565d4e611bf643b932accd1d592e87386ee15dc8a`  
Pixel 9a |  tegu_beta-ota-cp31.260618.005-a7115ba8.zip   
`a7115ba83df3a00d4a4670108e3ac00aff44d10a8928499a8257049b1e6a869b`  
Pixel 10 |  frankel_beta-ota-cp31.260618.005-a76e153d.zip   
`a76e153d990ccbc48e4a5cf89f7c13c171069a93aae23ca8bd113abcfab5ffdc`  
Pixel 10 Pro |  blazer_beta-ota-cp31.260618.005-1646fca2.zip   
`1646fca2434a24a85d0d40671069d7ab41280123b4e2d0582f7492bf704cb257`  
Pixel 10 Pro XL |  mustang_beta-ota-cp31.260618.005-8bedfcfc.zip   
`8bedfcfc8c01f57d67166bf5243ba9bd2042a89c4cd771811cf83db256d97515`  
Pixel 10 Pro Fold |  rango_beta-ota-cp31.260618.005-0ade2c66.zip   
`0ade2c66547ff36af143b5a870b32e7b3cf7612da3ce1672828e3cc1e29044d0`  
Pixel 10a |  stallion_beta-ota-cp31.260618.005-599f5b9c.zip   
`599f5b9c674b94b6ccb008ffd518bc9f49c959ef34e063ea8dba8e4301113741`  
  
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

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/oriole_beta-ota-cp31.260618.005-9485881d.zip)

_oriole_beta-ota-cp31.260618.005-9485881d.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/raven_beta-ota-cp31.260618.005-5bf3392a.zip)

_raven_beta-ota-cp31.260618.005-5bf3392a.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/bluejay_beta-ota-cp31.260618.005-d3320dd0.zip)

_bluejay_beta-ota-cp31.260618.005-d3320dd0.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/panther_beta-ota-cp31.260618.005-4bc68bd7.zip)

_panther_beta-ota-cp31.260618.005-4bc68bd7.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/cheetah_beta-ota-cp31.260618.005-99506ed1.zip)

_cheetah_beta-ota-cp31.260618.005-99506ed1.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/lynx_beta-ota-cp31.260618.005-656e629a.zip)

_lynx_beta-ota-cp31.260618.005-656e629a.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/felix_beta-ota-cp31.260618.005-3b0fc11c.zip)

_felix_beta-ota-cp31.260618.005-3b0fc11c.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/tangorpro_beta-ota-cp31.260618.005-4a2c6f2c.zip)

_tangorpro_beta-ota-cp31.260618.005-4a2c6f2c.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/shiba_beta-ota-cp31.260618.005-8514ac60.zip)

_shiba_beta-ota-cp31.260618.005-8514ac60.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/husky_beta-ota-cp31.260618.005-8dcacb35.zip)

_husky_beta-ota-cp31.260618.005-8dcacb35.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/akita_beta-ota-cp31.260618.005-0527f1ac.zip)

_akita_beta-ota-cp31.260618.005-0527f1ac.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/tokay_beta-ota-cp31.260618.005-8ab19d74.zip)

_tokay_beta-ota-cp31.260618.005-8ab19d74.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/caiman_beta-ota-cp31.260618.005-f071a5d0.zip)

_caiman_beta-ota-cp31.260618.005-f071a5d0.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/komodo_beta-ota-cp31.260618.005-52cc903a.zip)

_komodo_beta-ota-cp31.260618.005-52cc903a.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/comet_beta-ota-cp31.260618.005-29df0d9f.zip)

_comet_beta-ota-cp31.260618.005-29df0d9f.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/tegu_beta-ota-cp31.260618.005-a7115ba8.zip)

_tegu_beta-ota-cp31.260618.005-a7115ba8.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/frankel_beta-ota-cp31.260618.005-a76e153d.zip)

_frankel_beta-ota-cp31.260618.005-a76e153d.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/blazer_beta-ota-cp31.260618.005-1646fca2.zip)

_blazer_beta-ota-cp31.260618.005-1646fca2.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/mustang_beta-ota-cp31.260618.005-8bedfcfc.zip)

_mustang_beta-ota-cp31.260618.005-8bedfcfc.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/rango_beta-ota-cp31.260618.005-0ade2c66.zip)

_rango_beta-ota-cp31.260618.005-0ade2c66.zip_

## Download Android 17 OTA system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 OTA system image  [Download Android 17 OTA system image ](https://dl.google.com/developers/android/cinnamonbun/images/ota/stallion_beta-ota-cp31.260618.005-599f5b9c.zip)

_stallion_beta-ota-cp31.260618.005-599f5b9c.zip_

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
