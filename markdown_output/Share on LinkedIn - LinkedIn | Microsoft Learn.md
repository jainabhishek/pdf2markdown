# Share on LinkedIn - LinkedIn | Microsoft Learn

> Converted from PDF: Share on LinkedIn - LinkedIn | Microsoft Learn.pdf
> Conversion date: 2025-07-29 18:41:36

---

### <!-- Page 1 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM Share on LinkedIn 02/04/2025 Overview LinkedIn is a powerful platform to share content with your social network. Ensure your content receives the professional audience it deserves using Share on LinkedIn. Use Share on LinkedIn to: Get your content in front of an audience of millions of professionals. Drive traffic to your site and grow your member base. Benefit from having your content shared across multiple professional networks worldwide. Getting Started Authenticating Members New members Sharing on LinkedIn from your application for the first time will need to follow the Authenticating with OAuth 2.0 Guide. When requesting an authorization code in Step 2 of the OAuth 2.0 Guide, make sure to request the w_member_social scope! ﾉ Expand table Permission Name Description w_member_social Required to create a LinkedIn post on behalf of the authenticated member. After successful authentication, you will acquire an access token that can be used in the next step of the share process. https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 1 of 9

### | Share on LinkedIn

### 02/04/2025

# Overview

LinkedIn is a powerful platform to share content with your social network. Ensure your content

receives the professional audience it deserves using Share on LinkedIn.

### Use Share on LinkedIn to:

Get your content in front of an audience of millions of professionals.

Drive traffic to your site and grow your member base.

Benefit from having your content shared across multiple professional networks

worldwide.

### Getting Started

### Authenticating Members

New members Sharing on LinkedIn from your application for the first time will need to follow

the Authenticating with OAuth 2.0 Guide. When requesting an authorization code in Step 2 of

the OAuth 2.0 Guide, make sure to request the w_member_social scope!

### ﾉ Expand table

### Permission Name Description

w_member_social Required to create a LinkedIn post on behalf of the authenticated member.

After successful authentication, you will acquire an access token that can be used in the next

### step of the share process. |

### | --- |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 1 of 9 |

### | Permission Name Description |

### | --- |

| w_member_social Required to create a LinkedIn post on behalf of the authenticated member. |

### <!-- Page 2 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM If your application does not have this permission, you can add it through the Developer Portal . Select your app from My Apps , navigate to the Products tab, and add the Share on LinkedIn product which will grant you w_member_social. Creating a Share on LinkedIn There are multiple ways to share content with your LinkedIn network. In this guide, we will show you how to create shares using text, URLs, and images. For all shares created on LinkedIn, the request will always be a POST request to the User Generated Content (UGC) API. API Request HTTP POST https://api.linkedin.com/v2/ugcPosts ７ Note All requests require the following header: X-Restli-Protocol-Version: 2.0.0 Request Body Schema ﾉ Expand table Field Name Description Format Required author The author of a share contains Person URN of Person URN Yes the Member creating the share. See Sign In with LinkedIn using OpenID Connect to see how to retrieve the Person URN. lifecycleState Defines the state of the share. For the purposes string Yes of creating a share, the lifecycleState will always https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 2 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

| If your application does not have this permission, you can add it through the Developer Portal

. Select your app from My Apps , navigate to the Products tab, and add the Share on

LinkedIn product which will grant you w_member_social.

### Creating a Share on LinkedIn

There are multiple ways to share content with your LinkedIn network. In this guide, we will

show you how to create shares using text, URLs, and images. For all shares created on LinkedIn,

the request will always be a POST request to the User Generated Content (UGC) API.

### API Request

# HTTP

### POST https://api.linkedin.com/v2/ugcPosts

## ７ Note

### All requests require the following header: X-Restli-Protocol-Version: 2.0.0

### Request Body Schema

### ﾉ Expand table

### Field Name Description Format Required

author The author of a share contains Person URN of Person URN Yes

### the Member creating the share. See Sign In

### with LinkedIn using OpenID Connect to see

how to retrieve the Person URN.

lifecycleState Defines the state of the share. For the purposes string Yes

### of creating a share, the lifecycleState will always |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 2 of 9 |

### |  |

### | --- |

### |  |

### |  |

### |  |

### | --- |

### |  |

### |  |

# | HTTP |

### | --- |

### | POST https://api.linkedin.com/v2/ugcPosts |

### | Field Name Description Format Required |

### | --- |

| author The author of a share contains Person URN of Person URN Yes

### the Member creating the share. See Sign In

### with LinkedIn using OpenID Connect to see

### how to retrieve the Person URN. |

| lifecycleState Defines the state of the share. For the purposes string Yes

### of creating a share, the lifecycleState will always |

### | //learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page |

### <!-- Page 3 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM be PUBLISHED. specificContent Provides additional options while defining the ShareContent Yes content of the share. visibility Defines any visibility restrictions for the share. MemberNetworkVisibility Yes Possible values include: CONNECTIONS - The share will be viewable by 1st-degree connections only. PUBLIC - The share will be viewable by anyone on LinkedIn. Share Content ﾉ Expand table Field Name Description Format Required shareCommentary Provides the primary content for the share. string Yes shareMediaCategory Represents the media assets attached to the share. string Yes Possible values include: NONE - The share does not contain any media, and will only consist of text. ARTICLE - The share contains a URL. IMAGE - The Share contains an image. media If the shareMediaCategory is ARTICLE or IMAGE, ShareMedia[] No define those media assets here. Share Media ﾉ Expand table Field Description Format Required Name https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 3 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

| be PUBLISHED.

### specificContent Provides additional options while defining the ShareContent Yes

content of the share.

visibility Defines any visibility restrictions for the share. MemberNetworkVisibility Yes

### Possible values include:

### CONNECTIONS - The share will be viewable

by 1st-degree connections only.

### PUBLIC - The share will be viewable by

anyone on LinkedIn.

### Share Content

### ﾉ Expand table

### Field Name Description Format Required

shareCommentary Provides the primary content for the share. string Yes

shareMediaCategory Represents the media assets attached to the share. string Yes

### Possible values include:

### NONE - The share does not contain any media,

and will only consist of text.

ARTICLE - The share contains a URL.

IMAGE - The Share contains an image.

media If the shareMediaCategory is ARTICLE or IMAGE, ShareMedia[] No

define those media assets here.

### Share Media

### ﾉ Expand table

### Field Description Format Required

### Name |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 3 of 9 |

| on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12: |

### | --- |

### | be PUBLISHED. |

| specificContent Provides additional options while defining the ShareContent Yes

### content of the share. |

| visibility Defines any visibility restrictions for the share. MemberNetworkVisibility Yes

### Possible values include:

### CONNECTIONS - The share will be viewable

by 1st-degree connections only.

### PUBLIC - The share will be viewable by

### anyone on LinkedIn. |

### | Field Name Description Format Required |

### | --- |

| shareCommentary Provides the primary content for the share. string Yes |

| shareMediaCategory Represents the media assets attached to the share. string Yes

### Possible values include:

### NONE - The share does not contain any media,

and will only consist of text.

ARTICLE - The share contains a URL.

### IMAGE - The Share contains an image. |

| media If the shareMediaCategory is ARTICLE or IMAGE, ShareMedia[] No

### define those media assets here. |

### | Field Description Format Required

### Name |

### | --- |

### |  |

### <!-- Page 4 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM status Must be configured to READY. string Yes description Provide a short description for your image or article. string No media ID of the uploaded image asset. If you are uploading an DigitalMediaAsset No article, this field is not required. URN originalUrl Provide the URL of the article you would like to share here. string No title Customize the title of your image or article. string No Create a Text Share The example below creates a simple text Share on LinkedIn. Notice the visibility is set to PUBLIC, where anyone on the LinkedIn Platform can view this share. Sample Request Body JSON { "author": "urn:li:person:8675309", "lifecycleState": "PUBLISHED", "specificContent": { "com.linkedin.ugc.ShareContent": { "shareCommentary": { "text": "Hello World! This is my first Share on LinkedIn!" }, "shareMediaCategory": "NONE" } }, "visibility": { "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC" } } https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 4 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

### | status Must be configured to READY. string Yes

description Provide a short description for your image or article. string No

media ID of the uploaded image asset. If you are uploading an DigitalMediaAsset No

### article, this field is not required. URN

originalUrl Provide the URL of the article you would like to share here. string No

title Customize the title of your image or article. string No

### Create a Text Share

The example below creates a simple text Share on LinkedIn. Notice the visibility is set to

PUBLIC, where anyone on the LinkedIn Platform can view this share.

### Sample Request Body

# JSON

### {

### "author": "urn:li:person:8675309",

### "lifecycleState": "PUBLISHED",

### "specificContent": {

### "com.linkedin.ugc.ShareContent": {

### "shareCommentary": {

"text": "Hello World! This is my first Share on LinkedIn!"

### },

### "shareMediaCategory": "NONE"

### }

### },

### "visibility": {

### "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"

### }

### } |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 4 of 9 |

| on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12: |

### | --- |

### |  |

| status Must be configured to READY. string Yes |

| description Provide a short description for your image or article. string No |

| media ID of the uploaded image asset. If you are uploading an DigitalMediaAsset No

### article, this field is not required. URN |

| originalUrl Provide the URL of the article you would like to share here. string No |

| title Customize the title of your image or article. string No |

# | JSON |

### | --- |

### | {

### "author": "urn:li:person:8675309",

### "lifecycleState": "PUBLISHED",

### "specificContent": {

### "com.linkedin.ugc.ShareContent": {

### "shareCommentary": {

"text": "Hello World! This is my first Share on LinkedIn!"

### },

### "shareMediaCategory": "NONE"

### }

### },

### "visibility": {

### "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"

### }

### } |

### <!-- Page 5 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM Response A successful response will return 201 Created, and the newly created post will be identified by the X-RestLi-Id response header. Create an Article or URL Share The example below illustrates various options when Sharing an Article or URL. The request body is similar to the Text Share above, however, we have now specified a media parameter containing the URL, title, and description. Keep in mind the title and description are optional parameters. Sample Request Body JSON { "author": "urn:li:person:8675309", "lifecycleState": "PUBLISHED", "specificContent": { "com.linkedin.ugc.ShareContent": { "shareCommentary": { "text": "Learning more about LinkedIn by reading the LinkedIn Blog!" }, "shareMediaCategory": "ARTICLE", "media": [ { "status": "READY", "description": { "text": "Official LinkedIn Blog - Your source for insights and information about LinkedIn." }, "originalUrl": "https://blog.linkedin.com/", "title": { "text": "Official LinkedIn Blog" } } https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 5 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

### | Response

A successful response will return 201 Created, and the newly created post will be identified by

the X-RestLi-Id response header.

### Create an Article or URL Share

The example below illustrates various options when Sharing an Article or URL. The request

body is similar to the Text Share above, however, we have now specified a media parameter

containing the URL, title, and description. Keep in mind the title and description are optional

parameters.

### Sample Request Body

# JSON

### {

### "author": "urn:li:person:8675309",

### "lifecycleState": "PUBLISHED",

### "specificContent": {

### "com.linkedin.ugc.ShareContent": {

### "shareCommentary": {

### "text": "Learning more about LinkedIn by reading the

### LinkedIn Blog!"

### },

### "shareMediaCategory": "ARTICLE",

### "media": [

### {

### "status": "READY",

### "description": {

### "text": "Official LinkedIn Blog - Your source for

### insights and information about LinkedIn."

### },

### "originalUrl": "https://blog.linkedin.com/",

### "title": {

### "text": "Official LinkedIn Blog"

### }

### } |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 5 of 9 |

# | JSON |

### | --- |

### | {

### "author": "urn:li:person:8675309",

### "lifecycleState": "PUBLISHED",

### "specificContent": {

### "com.linkedin.ugc.ShareContent": {

### "shareCommentary": {

### "text": "Learning more about LinkedIn by reading the

### LinkedIn Blog!"

### },

### "shareMediaCategory": "ARTICLE",

### "media": [

### {

### "status": "READY",

### "description": {

### "text": "Official LinkedIn Blog - Your source for

### insights and information about LinkedIn."

### },

### "originalUrl": "https://blog.linkedin.com/",

### "title": {

### "text": "Official LinkedIn Blog"

### }

### } |

### | //learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page |

### <!-- Page 6 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM ] } }, "visibility": { "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC" } } Response A successful response will return 201 Created, and the newly created post will be identified by the X-RestLi-Id response header. Create an Image or Video Share If you'd like to attach an image or video to your share, you will first need to register, then upload your image/video to LinkedIn before the share can be created. We will walk through the following steps to create the share: 1. Register your image or video to be uploaded. 2. Upload your image or video to LinkedIn. 3. Create the image or video share. Register the Image or Video Send a POST request to the assets API, with the action query parameter to registerUpload. HTTP POST https://api.linkedin.com/v2/assets?action=registerUpload Similar to the author parameter we've used with the ugcPosts API, we will need to provide our Person URN. Additional recipes and serviceRelationships define the type of content we're https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 6 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

### | ]

### }

### },

### "visibility": {

### "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"

### }

### }

### Response

A successful response will return 201 Created, and the newly created post will be identified by

the X-RestLi-Id response header.

### Create an Image or Video Share

If you'd like to attach an image or video to your share, you will first need to register, then

upload your image/video to LinkedIn before the share can be created. We will walk through the

### following steps to create the share:

## 1. Register your image or video to be uploaded.

## 2. Upload your image or video to LinkedIn.

## 3. Create the image or video share.

### Register the Image or Video

Send a POST request to the assets API, with the action query parameter to registerUpload.

# HTTP

### POST https://api.linkedin.com/v2/assets?action=registerUpload

Similar to the author parameter we've used with the ugcPosts API, we will need to provide our

Person URN. Additional recipes and serviceRelationships define the type of content we're |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 6 of 9 |

| on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12: |

### | --- |

### | ]

### }

### },

### "visibility": {

### "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"

### }

### } |

# | HTTP |

### | --- |

### | POST https://api.linkedin.com/v2/assets?action=registerUpload |

### <!-- Page 7 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM publishing. For Share on LinkedIn, recipes will always contain either the type feedshare-image or the type feedshare-video (depending on which of the two you are uploading) and serviceRelationships will always define the relationshipType and identifier. See the request body below for reference. JSON { "registerUploadRequest": { "recipes": [ "urn:li:digitalmediaRecipe:feedshare-image" ], "owner": "urn:li:person:8675309", "serviceRelationships": [ { "relationshipType": "OWNER", "identifier": "urn:li:userGeneratedContent" } ] } } A successful response will contain an uploadUrl and asset that you will need to save for the next steps. JSON { "value": { "uploadMechanism": { "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest": { "headers": {}, "uploadUrl": "https://api.linkedin.com/mediaU‐ pload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feed‐ share&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMd‐ b2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1" } }, "mediaArtifact": "urn:li:digitalmediaMediaArtifact:(urn:li:digital‐ mediaAsset:C5522AQGTYER3k3ByHQ,urn:li:digitalmediaMediaArtifactClass:feed‐ share-uploadedImage)", "asset": "urn:li:digitalmediaAsset:C5522AQGTYER3k3ByHQ" } https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 7 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

| publishing. For Share on LinkedIn, recipes will always contain either the type feedshare-image

or the type feedshare-video (depending on which of the two you are uploading) and

serviceRelationships will always define the relationshipType and identifier. See the request body

below for reference.

# JSON

### {

### "registerUploadRequest": {

### "recipes": [

### "urn:li:digitalmediaRecipe:feedshare-image"

### ],

### "owner": "urn:li:person:8675309",

### "serviceRelationships": [

### {

### "relationshipType": "OWNER",

### "identifier": "urn:li:userGeneratedContent"

### }

### ]

### }

### }

A successful response will contain an uploadUrl and asset that you will need to save for the

next steps.

# JSON

### {

### "value": {

### "uploadMechanism": {

### "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest": {

### "headers": {},

### "uploadUrl": "https://api.linkedin.com/mediaU‐

### pload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feed‐

### share&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMd‐

### b2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1"

### }

### },

### "mediaArtifact": "urn:li:digitalmediaMediaArtifact:(urn:li:digital‐

### mediaAsset:C5522AQGTYER3k3ByHQ,urn:li:digitalmediaMediaArtifactClass:feed‐

### share-uploadedImage)",

### "asset": "urn:li:digitalmediaAsset:C5522AQGTYER3k3ByHQ"

### } |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 7 of 9 |

# | JSON |

### | --- |

### | {

### "registerUploadRequest": {

### "recipes": [

### "urn:li:digitalmediaRecipe:feedshare-image"

### ],

### "owner": "urn:li:person:8675309",

### "serviceRelationships": [

### {

### "relationshipType": "OWNER",

### "identifier": "urn:li:userGeneratedContent"

### }

### ]

### }

### } |

# | JSON |

### | --- |

### | {

### "value": {

### "uploadMechanism": {

### "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest": {

### "headers": {},

### "uploadUrl": "https://api.linkedin.com/mediaU‐

### pload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feed‐

### share&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMd‐

### b2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1"

### }

### },

### "mediaArtifact": "urn:li:digitalmediaMediaArtifact:(urn:li:digital‐

### mediaAsset:C5522AQGTYER3k3ByHQ,urn:li:digitalmediaMediaArtifactClass:feed‐

### share-uploadedImage)",

### "asset": "urn:li:digitalmediaAsset:C5522AQGTYER3k3ByHQ"

### } |

### | //learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page |

### <!-- Page 8 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM } Upload Image or Video Binary File Using the uploadUrl returned from Step 1, upload your image or video to LinkedIn. To upload your image or video, send a POST request to the uploadUrl with your image or video included as a binary file. The example below uses cURL to upload an image file. Sample Request Bash curl -i --upload-file /Users/peter/Desktop/superneatimage.png --header "Au‐ thorization: Bearer redacted" 'https://api.linkedin.com/mediaU‐ pload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feed‐ share&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMd‐ b2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1' Create the Image or Video Share After the image or video file has successfully uploaded from Step 2, we will use the asset from Step 1 to attach the image to our share. Below is a sample request for an image; for a video, the shareMediaCategory should be VIDEO instead of IMAGE. Sample Request Body JSON { "author": "urn:li:person:8675309", "lifecycleState": "PUBLISHED", "specificContent": { "com.linkedin.ugc.ShareContent": { "shareCommentary": { https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 8 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

### | }

### Upload Image or Video Binary File

Using the uploadUrl returned from Step 1, upload your image or video to LinkedIn. To upload

your image or video, send a POST request to the uploadUrl with your image or video included

as a binary file. The example below uses cURL to upload an image file.

### Sample Request

### Bash

### curl -i --upload-file /Users/peter/Desktop/superneatimage.png --header "Au‐

### thorization: Bearer redacted" 'https://api.linkedin.com/mediaU‐

### pload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feed‐

### share&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMd‐

### b2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1'

### Create the Image or Video Share

After the image or video file has successfully uploaded from Step 2, we will use the asset from

Step 1 to attach the image to our share. Below is a sample request for an image; for a video, the

shareMediaCategory should be VIDEO instead of IMAGE.

### Sample Request Body

# JSON

### {

### "author": "urn:li:person:8675309",

### "lifecycleState": "PUBLISHED",

### "specificContent": {

### "com.linkedin.ugc.ShareContent": {

### "shareCommentary": { |

| https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 8 of 9 |

| on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12: |

### | --- |

### | } |

### | Bash |

### | --- |

### | curl -i --upload-file /Users/peter/Desktop/superneatimage.png --header "Au‐

### thorization: Bearer redacted" 'https://api.linkedin.com/mediaU‐

### pload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feed‐

### share&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMd‐

### b2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1' |

# | JSON |

### | --- |

### | {

### "author": "urn:li:person:8675309",

### "lifecycleState": "PUBLISHED",

### "specificContent": {

### "com.linkedin.ugc.ShareContent": {

### "shareCommentary": { |

### | //learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page |

### <!-- Page 9 -->

Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM "text": "Feeling inspired after meeting so many talented individuals at this year's conference. #talentconnect" }, "shareMediaCategory": "IMAGE", "media": [ { "status": "READY", "description": { "text": "Center stage!" }, "media": "urn:li:digitalmediaAsset:C5422AQEbc381YmIu‐ vg", "title": { "text": "LinkedIn Talent Connect 2021" } } ] } }, "visibility": { "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC" } } Response A successful response will return 201 Created, and the newly created post will be identified by the X-RestLi-Id response header. Rate Limits ﾉ Expand table Throttle Type Daily Request Limit (UTC ) Member 150 Requests Application 100,000 Requests https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin Page 9 of 9

| Share on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12:43 PM |

### | --- |

### | "text": "Feeling inspired after meeting so many talented

### individuals at this year's conference. #talentconnect"

### },

### "shareMediaCategory": "IMAGE",

### "media": [

### {

### "status": "READY",

### "description": {

### "text": "Center stage!"

### },

### "media": "urn:li:digitalmediaAsset:C5422AQEbc381YmIu‐

### vg",

### "title": {

### "text": "LinkedIn Talent Connect 2021"

### }

### }

### ]

### }

### },

### "visibility": {

### "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"

### }

### }

### Response

A successful response will return 201 Created, and the newly created post will be identified by

the X-RestLi-Id response header.

### Rate Limits

### ﾉ Expand table

### Throttle Type Daily Request Limit (UTC )

### Member 150 Requests

### Application 100,000 Requests |

| on LinkedIn - LinkedIn | Microsoft Learn 7/27/25, 12: |

### | --- |

### | "text": "Feeling inspired after meeting so many talented

### individuals at this year's conference. #talentconnect"

### },

### "shareMediaCategory": "IMAGE",

### "media": [

### {

### "status": "READY",

### "description": {

### "text": "Center stage!"

### },

### "media": "urn:li:digitalmediaAsset:C5422AQEbc381YmIu‐

### vg",

### "title": {

### "text": "LinkedIn Talent Connect 2021"

### }

### }

### ]

### }

### },

### "visibility": {

### "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"

### }

### } |

### | Throttle Type Daily Request Limit (UTC ) |

### | --- |

### | Member 150 Requests |

### | Application 100,000 Requests |

### |  |

### | --- |

### |  |

### |  |
