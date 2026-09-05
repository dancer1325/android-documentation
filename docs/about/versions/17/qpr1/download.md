# Factory images for Google Pixel  |  Android Developers

**Source:** [https://developer.android.com/about/versions/17/qpr1/download](https://developer.android.com/about/versions/17/qpr1/download)

---

  * [ Android Developers ](https://developer.android.com/)
  * [ Essentials ](https://developer.android.com/get-started)
  * [ Releases ](https://developer.android.com/about/versions)



#  Factory images for Google Pixel Stay organized with collections  Save and categorize content based on your preferences. 

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

Connect your device over USB, then navigate to Android Flash Tool using the following link and follow the onscreen guidance: <https://flash.android.com/preview/cinnamonbun-qpr1-beta6>.

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
Pixel 6 |  oriole_beta-cp31.260618.005-factory-e13001cc.zip   
`e13001cc911f55e283c62533ee5c94870557c118130422d7bfb1db0b22226be5`  
Pixel 6 Pro |  raven_beta-cp31.260618.005-factory-6cb8278d.zip   
`6cb8278dfd40385cb42a37437ac147c351d3de2288a2f9b9bf7c58eb8358e37d`  
Pixel 6a |  bluejay_beta-cp31.260618.005-factory-7f4cbce5.zip   
`7f4cbce5e813ebdaa4477af4c15a98beb83802563cdd0263d0ea0aea949a75f9`  
Pixel 7 |  panther_beta-cp31.260618.005-factory-5847ab57.zip   
`5847ab5753227e56c2b4117bddc4139d04e9500aa69ffa9cffad769cb379c16e`  
Pixel 7 Pro |  cheetah_beta-cp31.260618.005-factory-122b96ef.zip   
`122b96ef0aeec256a7d9c10e3b2e3928cb6f4a0d005c2113f16c97c8514ccf92`  
Pixel 7a |  lynx_beta-cp31.260618.005-factory-20055463.zip   
`20055463e4b9623ed4a6a09162ecf6443ba461891396344c2c821df9b434b4e2`  
Pixel Fold |  felix_beta-cp31.260618.005-factory-2bb41653.zip   
`2bb4165364648a1e887f4ae4440d4cadafa08d8302e47b015ce2ec442a5f51de`  
Pixel Tablet |  tangorpro_beta-cp31.260618.005-factory-ddcab631.zip   
`ddcab63181cdef86a16a7fb129e012f614955abe0f4c7a1b9f444fd08a4734aa`  
Pixel 8 |  shiba_beta-cp31.260618.005-factory-a5603443.zip   
`a5603443473faf16028cc817f6e2c6658e816ec339146f4643deb81b5eff0340`  
Pixel 8 Pro |  husky_beta-cp31.260618.005-factory-1f929d40.zip   
`1f929d40466f4e0f491c9f2ee110cf46f3a9a6a73fc48a100a9dd947d9e86d03`  
Pixel 8a |  akita_beta-cp31.260618.005-factory-efb8fcb9.zip   
`efb8fcb908c041fe8c3fb5c8b05731d91ee2ed7ac7b90798d1f7ecde1960442c`  
Pixel 9 |  tokay_beta-cp31.260618.005-factory-bede7edb.zip   
`bede7edbe52d76132ef459306fe40aa62569c54fbc36f6a25a006435f44a5368`  
Pixel 9 Pro |  caiman_beta-cp31.260618.005-factory-abcc8b78.zip   
`abcc8b7882f2594608007b94c97da1afc73f4430f3c691e35fbbce3903e03479`  
Pixel 9 Pro XL |  komodo_beta-cp31.260618.005-factory-83c63c7e.zip   
`83c63c7e9caffdeb15f478967faf5336712f832c318c5b30d05325fc5defbe2c`  
Pixel 9 Pro Fold |  comet_beta-cp31.260618.005-factory-6d56ed50.zip   
`6d56ed507d183678b4735273f8a587615650325ab929eda11e40d2d92036dd7e`  
Pixel 9a |  tegu_beta-cp31.260618.005-factory-17a3b9e1.zip   
`17a3b9e15d0320d4d29e20e98a57d11dd55af0cbb831dc1f5a05d4db3ec3901b`  
Pixel 10 |  frankel_beta-cp31.260618.005-factory-3528fb1f.zip   
`3528fb1fe7afcb98133b6bf7cb5684abf9be239e63407e58f13e7c69d91b5e10`  
Pixel 10 Pro |  blazer_beta-cp31.260618.005-factory-dac9f395.zip   
`dac9f3956447aa0e4ba42b54e38e1fdd2a04664f226d7727cf89c4ed399c6cb4`  
Pixel 10 Pro XL |  mustang_beta-cp31.260618.005-factory-e3d450b9.zip   
`e3d450b92c06d9ddae068aed53b1a2816ec5bd7fbdef9605d045a08feb2f711e`  
Pixel 10 Pro Fold |  rango_beta-cp31.260618.005-factory-dd7686d0.zip   
`dd7686d0cca306a7590db622e1b39efb5b6b6c5250f806bfb08a67af878c7f65`  
Pixel 10a |  stallion_beta-cp31.260618.005-factory-35b7fed6.zip   
`35b7fed699fe8140f9f7eedf37db94a3744ffd2effd9ccef12fbf64fd4d96df1`  
  
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

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/oriole_beta-cp31.260618.005-factory-e13001cc.zip)

_oriole_beta-cp31.260618.005-factory-e13001cc.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/raven_beta-cp31.260618.005-factory-6cb8278d.zip)

_raven_beta-cp31.260618.005-factory-6cb8278d.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/bluejay_beta-cp31.260618.005-factory-7f4cbce5.zip)

_bluejay_beta-cp31.260618.005-factory-7f4cbce5.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/panther_beta-cp31.260618.005-factory-5847ab57.zip)

_panther_beta-cp31.260618.005-factory-5847ab57.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/cheetah_beta-cp31.260618.005-factory-122b96ef.zip)

_cheetah_beta-cp31.260618.005-factory-122b96ef.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/lynx_beta-cp31.260618.005-factory-20055463.zip)

_lynx_beta-cp31.260618.005-factory-20055463.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/felix_beta-cp31.260618.005-factory-2bb41653.zip)

_felix_beta-cp31.260618.005-factory-2bb41653.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/tangorpro_beta-cp31.260618.005-factory-ddcab631.zip)

_tangorpro_beta-cp31.260618.005-factory-ddcab631.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/shiba_beta-cp31.260618.005-factory-a5603443.zip)

_shiba_beta-cp31.260618.005-factory-a5603443.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/husky_beta-cp31.260618.005-factory-1f929d40.zip)

_husky_beta-cp31.260618.005-factory-1f929d40.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/akita_beta-cp31.260618.005-factory-efb8fcb9.zip)

_akita_beta-cp31.260618.005-factory-efb8fcb9.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/tokay_beta-cp31.260618.005-factory-bede7edb.zip)

_tokay_beta-cp31.260618.005-factory-bede7edb.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/caiman_beta-cp31.260618.005-factory-abcc8b78.zip)

_caiman_beta-cp31.260618.005-factory-abcc8b78.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/komodo_beta-cp31.260618.005-factory-83c63c7e.zip)

_komodo_beta-cp31.260618.005-factory-83c63c7e.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/comet_beta-cp31.260618.005-factory-6d56ed50.zip)

_comet_beta-cp31.260618.005-factory-6d56ed50.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/tegu_beta-cp31.260618.005-factory-17a3b9e1.zip)

_tegu_beta-cp31.260618.005-factory-17a3b9e1.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/frankel_beta-cp31.260618.005-factory-3528fb1f.zip)

_frankel_beta-cp31.260618.005-factory-3528fb1f.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/blazer_beta-cp31.260618.005-factory-dac9f395.zip)

_blazer_beta-cp31.260618.005-factory-dac9f395.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/mustang_beta-cp31.260618.005-factory-e3d450b9.zip)

_mustang_beta-cp31.260618.005-factory-e3d450b9.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/rango_beta-cp31.260618.005-factory-dd7686d0.zip)

_rango_beta-cp31.260618.005-factory-dd7686d0.zip_

## Download Android 17 factory system image

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By clicking to accept, you hereby agree to the following:  
  
All use of this development version SDK will be governed by the Android Software Development Kit License Agreement (available at https://developer.android.com/studio/terms and such URL may be updated or changed by Google from time to time), which will terminate when Google issues a final release version.  
  
Your testing and feedback are important part of the development process and by using the SDK, you acknowledge that (i) implementation of some features are still under development, (ii) you should not rely on the SDK having the full functionality of a stable release; (iii) you agree not to publicly distribute or ship any application using this SDK as this SDK will no longer be supported after the official Android SDK is released; and (iv) you agree that Google may deliver elements of the SDK to your devices via auto-update (OTA or otherwise, in each case as determined by Google).  
  
WITHOUT LIMITING SECTION 10 OF THE ANDROID SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT, YOU UNDERSTAND THAT A DEVELOPMENT VERSION OF A SDK IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE. 

I have read and agree with the above terms and conditions

Download Android 17 factory system image  [Download Android 17 factory system image ](https://dl.google.com/developers/android/cinnamonbun/images/factory/stallion_beta-cp31.260618.005-factory-35b7fed6.zip)

_stallion_beta-cp31.260618.005-factory-35b7fed6.zip_

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
