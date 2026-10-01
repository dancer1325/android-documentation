# Other Play guides  |  Android Developers

**Source:** [https://developer.android.com/guide/playcore/asset-delivery](https://developer.android.com/guide/playcore/asset-delivery)

---

Save and categorize content based on your preferences. 

###  Play Asset Delivery 

_Play Asset Delivery (PAD)_ brings the benefits of app bundles to games. It allows games larger than 200MB to replace legacy expansion files (OBBs) by publishing a single artifact to Play containing all the resources the game needs. PAD offers flexible delivery modes, auto-updates, compression, and delta patching, and is free to use. Using PAD, all asset packs are hosted and served on Google Play removing the need to use a content delivery network (CDN) to get your game resources to players.

Play Asset Delivery uses asset packs, which are composed of assets (such as textures, shaders, and sounds), but no executable code. Through Dynamic Delivery, you can customize how and when each asset pack is downloaded onto a device according to three delivery modes: install-time, fast-follow, and on-demand.

If you want to jump directly to implementing PAD in your game, see Next step.

![](https://developer.android.com/static/images/picto-icons/distribution.svg)

#### Single publishing artifact

Publish a single artifact to Play including all your game's resources 

![](https://developer.android.com/static/images/picto-icons/pathway.svg)

#### Flexible delivery modes

Control when and how Play delivers your game assets 

![](https://developer.android.com/static/images/picto-icons/frame.svg)

#### Texture compression format targeting

Start making efficient use of the available hardware while not sacrificing reach 

![](https://developer.android.com/static/images/spot-icons/tools-update.svg)

#### Automatic updates

Let Play auto-update your game assets with advanced compression and delta patching 

[ ![](https://developer.android.com/static/images/distribute/stories/Devsisters_PAD_thumbnail.png) ](https://developer.android.com/stories/games/devsisters)

Case Study

#### Cookie Run: OvenBreak saves over $200K CDN cost with Play Asset Delivery

Devsisters is a mobile game developer and publisher, producing casual games based on the Cookie Run IP. Learn how they decreased their game's unnecessary resources with Play Asset Delivery. 

[Learn more](https://developer.android.com/stories/games/devsisters)

[ ![](https://developer.android.com/static/images/cards/distribute/stories/cat-daddy-games-logo.png) ](https://developer.android.com/stories/games/cat-daddy)

Case Study

#### 2K delivers higher quality graphics with Play Asset Delivery

Cat Daddy Games is a wholly-owned 2K studio based in Kirkland, Washington. The teams behind the NBA 2K Mobile, NBA SuperCard, and WWE SuperCard series were looking for a solution to improve the overall quality of their games for users, 

[Learn more](https://developer.android.com/stories/games/cat-daddy)

[ ![](https://developer.android.com/static/images/cards/distribute/stories/cdpr-thumbnail.png) ](https://developer.android.com/stories/games/cdpr)

Case Study

#### CD Projekt RED reduces update size by 90% and increases update rates by 10% with Play Asset Delivery

Based in Warsaw, Poland, game developer CD Projekt RED (CDPR) reimagined their mini-game in The Witcher 3, GWENT: The Witcher Card Game, to launch as a standalone free-to-play title on Google Play in March of 2020. 

[Learn more](https://developer.android.com/stories/games/cdpr)

[ ![](https://developer.android.com/static/images/cards/distribute/stories/puzzle-kids-framed.png) ](https://developer.android.com/stories/games/rv-appstudios-pad)

Case study

#### RV AppStudios improves user retention with Google Play Asset Delivery

US-based developer RV AppStudios has over 200 million downloads to date across their portfolio of casual games, educational kids apps, and utility apps. 

[Learn more](https://developer.android.com/stories/games/rv-appstudios-pad)

[ ![](https://developer.android.com/static/images/cards/distribute/stories/gameloft-asphalt8.jpg) ](https://developer.android.com/stories/games/gameloft-pad)

Case study

#### Gameloft acquires 10% more new users with Google Play Asset Delivery

In 2000, Gameloft was created with a passion for games and a desire to bring them to players around the world. 

[Learn more](https://developer.android.com/stories/games/gameloft-pad)

Video

#### Google Play Asset Delivery for games

Optimize your game delivery with the new App Bundle for games, which enables free, customizable delivery of large game assets. 

[Watch on YouTube](https://www.youtube.com/watch?v=WW9GevpEo1s)

Content and code samples on this page are subject to the licenses described in the [Content License](/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-18 UTC."],[],[]] 
