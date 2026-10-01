# Factory images for Google Pixel  |  Android Developers

**Source:** [https://developer.android.com/about/versions/17/qpr1/download](https://developer.android.com/about/versions/17/qpr1/download)

---

#  Factory images for Google Pixel Save and categorize content based on your preferences. 

If you are a developer with a supported Google Pixel device, you can manually update that device to the latest build for testing and development. Flashing a factory image requires a full device reset, so make sure to [back up your data](https://support.google.com/pixelphone/answer/7179901) first. Builds are available for the following Pixel devices:

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

After you've flashed a beta build to your Pixel device, your device is automatically enrolled in the [Android Beta for Pixel program](https://g.co/androidBeta) and offered continuous over-the-air (OTA) updates to the latest beta builds (including QPRs) until you choose to unenroll that device from the program. We also deliver flashable images at each milestone, so you can choose the approach that works best for your test environment. 

Use the following links and instructions to update your supported device to the latest build. See [Get Android 17 QPR beta builds](/about/versions/17/get-qpr) for other ways to get QPR1 for testing and development.

**Warning:** Flashing to a beta build from a production build—or going back to a production build from a beta build—requires a full device reset that removes all user data on the device. Make sure to [back up the data from your Pixel](https://support.google.com/pixelphone/answer/7179901) first.

## Flash your device using Android Flash Tool

**Android Flash Tool** lets you securely flash a system image to your supported Pixel device. Android Flash Tool works with any Web browser that supports WebUSB, such as Chrome or Edge 79+.

Android Flash Tool guides you step-by-step through the process of flashing your device—there's no need to have tools installed—but you do need to unlock your device and [enable USB Debugging in Developer options](/studio/debug/dev-options#enable). For complete instructions, see the [Android Flash Tool documentation](https://source.android.com/setup/contribute/flash).

Connect your device over USB, then navigate to Android Flash Tool using the following link and follow the onscreen guidance: <https://flash.android.com/preview/cinnamonbun-qpr1-beta9>.

## Flash your device manually

![](/static/images/lockups/android-stacked.svg)

You can also download the latest system image and manually flash it to your device. See the following table to download the system image for your test device. Manually flashing a device is useful if you need precise control over the test environment or if you need to reinstall frequently, such as when performing automated testing.

After you back up your device data and download the matching system image, you can [flash the image onto your device](https://developers.google.com/android/images#instructions).

You can choose to return to the latest public build at any time.

### Device factory images

**Release date** | June 1, 2026  
---|---  
**Builds** | CP21.260330.011  
**Emulator support** | x86 (64-bit), ARM (v8-A)  
**Security patch level** | 2026-05-05  
**Google Play services** | 26.11.36  
Device | Download Link and SHA-256 Checksum  
---|---  
Pixel 6 |  oriole_beta-cp31.260623.012-factory-d3240665.zip   
`d324066576795fe8d1180219d795568a18b5f0956bf45a07bbbb72bf4ccde799`  
Pixel 6 Pro |  raven_beta-cp31.260623.012-factory-61b11097.zip   
`61b11097e76586904c0fe12ace62d19f5e65b9e5717d6e65f11c977a7bab29a2`  
Pixel 6a |  bluejay_beta-cp31.260623.012-factory-4fcbcf6b.zip   
`4fcbcf6b6db90868eb7d550fb1b9707230b98e1fbe61ede98e00103d66de1d92`  
Pixel 7 |  panther_beta-cp31.260623.012-factory-09adcc9f.zip   
`09adcc9f1e07413cc8ab5c0200b78bb6045d9f15879e0b4ba0710debfa95ad2c`  
Pixel 7 Pro |  cheetah_beta-cp31.260623.012-factory-595b606d.zip   
`595b606de45a9f1077ef8a2fc293deccdc042fe26c2398582ff5ddd3527c0f8b`  
Pixel 7a |  lynx_beta-cp31.260623.012-factory-5c0f96dc.zip   
`5c0f96dc84cac09d6f1e73494d1af9534b6f430ccc7da9be434f62cd4763a98f`  
Pixel Fold |  felix_beta-cp31.260623.012-factory-88fa7e29.zip   
`88fa7e2989430d0b89a49b03ccca7c0dfd116104a00d02b91f60ad89196b8063`  
Pixel Tablet |  tangorpro_beta-cp31.260623.012-factory-19308669.zip   
`19308669b1324cc05893d36495186843950180f5c3701bc5a5a3ccb7d6c0d04a`  
Pixel 8 |  shiba_beta-cp31.260623.012-factory-cfbe2993.zip   
`cfbe29935bcf4f386b0ff9d21674937eb220eed682e41432f641e2eaa9c64fe3`  
Pixel 8 Pro |  husky_beta-cp31.260623.012-factory-5da70299.zip   
`5da702997f81d3d1b51379fe31ed3aca5e87b64b3525612cfadc3fd57546c863`  
Pixel 8a |  akita_beta-cp31.260623.012-factory-3fcb27e2.zip   
`3fcb27e286e71180460f5c320b37cbceba8204882d31cd28034de6cb402f9c29`  
Pixel 9 |  tokay_beta-cp31.260623.012-factory-b6e5f071.zip   
`b6e5f071a564457437a949b92310ec28925b845c95965f85523a21f975495966`  
Pixel 9 Pro |  caiman_beta-cp31.260623.012-factory-209a52b6.zip   
`209a52b698ea3519ef85b86473ad15921fa7849d11373f22039d7a30264b972a`  
Pixel 9 Pro XL |  komodo_beta-cp31.260623.012-factory-8042999e.zip   
`8042999e7202419053f7f8d290ab09fe2568d748bc1b65092ed09762c4584e8b`  
Pixel 9 Pro Fold |  comet_beta-cp31.260623.012-factory-c0b71bbb.zip   
`c0b71bbb0fe428b42787b31393f84bfd39c4b989fef93ba9dcf859ab3f1923d6`  
Pixel 9a |  tegu_beta-cp31.260623.012-factory-cf99ed2b.zip   
`cf99ed2bcfe70d6297db5ab80df38d631e0fe85393672ed035c6061117486964`  
Pixel 10 |  frankel_beta-cp31.260623.012-factory-cbfd0e77.zip   
`cbfd0e77b619a38dc0cf7d7b68be70350f3ba7956150cdf180c021e6e99170d0`  
Pixel 10 Pro |  blazer_beta-cp31.260623.012-factory-fee6c2fd.zip   
`fee6c2fd6e6a4e83d97614442b0dd69cd808daa973e7cb64922feccb5fb79286`  
Pixel 10 Pro XL |  mustang_beta-cp31.260623.012-factory-921f59c9.zip   
`921f59c901c56935abafb4e4a6ad950e274b9bf0b8c795795ab22b484bd3e540`  
Pixel 10 Pro Fold |  rango_beta-cp31.260623.012-factory-b34f5b1e.zip   
`b34f5b1e6cfee17b4033cc7005914e1f39e1afedb26ff2bdca891ccff0171b12`  
Pixel 10a |  stallion_beta-cp31.260623.012-factory-32568ad2.zip   
`32568ad2ae019de92a4066077b5c8ac842f4bc13e3c7d6369416ef2f01252fbb`  
  
## Return to a public build

You can either use the Android Flash Tool to [flash the factory image](https://flash.android.com/back-to-public), or obtain a factory spec system image from the [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images) page and then manually flash it to the device.

**Warning:** Going back to a public build from a preview build (Developer Preview or Beta) requires a full device reset that removes all user data on the device. Make sure to [back up your data first](https://support.google.com/pixelphone/answer/7179901).

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/oriole_beta-cp31.260623.012-factory-d3240665.zip)

_oriole_beta-cp31.260623.012-factory-d3240665.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/raven_beta-cp31.260623.012-factory-61b11097.zip)

_raven_beta-cp31.260623.012-factory-61b11097.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/bluejay_beta-cp31.260623.012-factory-4fcbcf6b.zip)

_bluejay_beta-cp31.260623.012-factory-4fcbcf6b.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp31.260623.012-factory-09adcc9f.zip)

_panther_beta-cp31.260623.012-factory-09adcc9f.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp31.260623.012-factory-595b606d.zip)

_cheetah_beta-cp31.260623.012-factory-595b606d.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp31.260623.012-factory-5c0f96dc.zip)

_lynx_beta-cp31.260623.012-factory-5c0f96dc.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp31.260623.012-factory-88fa7e29.zip)

_felix_beta-cp31.260623.012-factory-88fa7e29.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp31.260623.012-factory-19308669.zip)

_tangorpro_beta-cp31.260623.012-factory-19308669.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp31.260623.012-factory-cfbe2993.zip)

_shiba_beta-cp31.260623.012-factory-cfbe2993.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp31.260623.012-factory-5da70299.zip)

_husky_beta-cp31.260623.012-factory-5da70299.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp31.260623.012-factory-3fcb27e2.zip)

_akita_beta-cp31.260623.012-factory-3fcb27e2.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp31.260623.012-factory-b6e5f071.zip)

_tokay_beta-cp31.260623.012-factory-b6e5f071.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp31.260623.012-factory-209a52b6.zip)

_caiman_beta-cp31.260623.012-factory-209a52b6.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp31.260623.012-factory-8042999e.zip)

_komodo_beta-cp31.260623.012-factory-8042999e.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp31.260623.012-factory-c0b71bbb.zip)

_comet_beta-cp31.260623.012-factory-c0b71bbb.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp31.260623.012-factory-cf99ed2b.zip)

_tegu_beta-cp31.260623.012-factory-cf99ed2b.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp31.260623.012-factory-cbfd0e77.zip)

_frankel_beta-cp31.260623.012-factory-cbfd0e77.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp31.260623.012-factory-fee6c2fd.zip)

_blazer_beta-cp31.260623.012-factory-fee6c2fd.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp31.260623.012-factory-921f59c9.zip)

_mustang_beta-cp31.260623.012-factory-921f59c9.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp31.260623.012-factory-b34f5b1e.zip)

_rango_beta-cp31.260623.012-factory-b34f5b1e.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/stallion_beta-cp31.260623.012-factory-32568ad2.zip)

_stallion_beta-cp31.260623.012-factory-32568ad2.zip_

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-16 UTC."],[],[]] 
