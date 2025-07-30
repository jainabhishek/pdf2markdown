
<style>
/* Enhanced PDF-to-Markdown Styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.3em;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    border: 1px solid #ddd;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #f8f9fa;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.page-break {
    page-break-before: always;
    border-top: 2px dashed #ccc;
    margin: 2em 0;
    padding-top: 1em;
}

small {
    font-size: 0.85em;
    color: #666;
}

blockquote {
    border-left: 4px solid #ddd;
    margin: 1em 0;
    padding-left: 1em;
    color: #666;
}

.image-container {
    text-align: center;
    margin: 1em 0;
}

.image-container img {
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>


# LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn

> **Enhanced Conversion** from PDF: `LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn.pdf`  
> Conversion date: 2025-07-29 19:10:32  
> Pages: 14  
> Images extracted: 5  

---


<!-- Page 1 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### Authorization Code Flow (3-legged

#### OAuth)

#### 11/30/2023

The Authorization Code Flow is used for applications to request permission from a LinkedIn

member to access their account data. The level of access or profile detail is explicitly requested

using the scope parameter during the authorization process outlined below. This workflow will

send a consent prompt to a selected member, and once approved your application may begin

#### making API calls on behalf of that member.

This approval process ensures that LinkedIn members are aware of what level of detail an

application may access or action it may perform on their behalf.

If multiple scopes are requested, the user must be consent to all of them and may not select

individual scopes. For the benefit of your LinkedIn users, please ensure that your application

#### requests the least number of scope permissions.

#### ７ Note

#### Generate a Token Manually Using the Developer Portal

The LinkedIn Developer Portal has a token generator for manually creating tokens. Visit

the LinkedIn Developer Portal Token Generator or follow the steps outlined in

#### Developer Portal Tools.

#### Authorization Code Flow

1. Configure your application in the Developer Portal to obtain Client ID and Client Secret.

2. Your application directs the browser to LinkedIn's OAuth 2.0 authorization page where the

#### member authenticates.

3. After authentication, LinkedIn's authorization server passes an authorization code to your

#### application.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 1 of 14


| Authorization Code Flow (3-legged
OAuth)
11/30/2023
The Authorization Code Flow is used for applications to request permission from a LinkedIn
member to access their account data. The level of access or profile detail is explicitly requested
using the scope parameter during the authorization process outlined below. This workflow will
send a consent prompt to a selected member, and once approved your application may begin
making API calls on behalf of that member.
This approval process ensures that LinkedIn members are aware of what level of detail an
application may access or action it may perform on their behalf.
If multiple scopes are requested, the user must be consent to all of them and may not select
individual scopes. For the benefit of your LinkedIn users, please ensure that your application
requests the least number of scope permissions.
７ Note
Generate a Token Manually Using the Developer Portal
The LinkedIn Developer Portal has a token generator for manually creating tokens. Visit
the LinkedIn Developer Portal Token Generator or follow the steps outlined in
Developer Portal Tools.
Authorization Code Flow
1. Configure your application in the Developer Portal to obtain Client ID and Client Secret.
2. Your application directs the browser to LinkedIn's OAuth 2.0 authorization page where the
member authenticates.
3. After authentication, LinkedIn's authorization server passes an authorization code to your
application. |
| --- |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 1 of 14 |


|  |
| --- |


<!-- Page 2 -->
<div class="image-container">
<img src="images/LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn_page_2_img_1.png" alt="Image from page 2">
</div>

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

4. Your application sends this code to LinkedIn and LinkedIn returns an access token.

5. Your application uses this token to make API calls on behalf of the member.

#### How to Implement 3-legged OAuth

Follow the steps given below to implement the 3-legged OAuth for LinkedIn APIs:

#### Prerequisites

A LinkedIn Developer application to create a new application or select your existing

#### application

Prior authorization access granted for at least one 3-legged OAuth permission.

The permission request workflow is outlined in the Getting Access section.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 2 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| 4. Your application sends this code to LinkedIn and LinkedIn returns an access token.
5. Your application uses this token to make API calls on behalf of the member.
How to Implement 3-legged OAuth
Follow the steps given below to implement the 3-legged OAuth for LinkedIn APIs:
Prerequisites
A LinkedIn Developer application to create a new application or select your existing
application
Prior authorization access granted for at least one 3-legged OAuth permission.
The permission request workflow is outlined in the Getting Access section. |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 2 of 14 |


|  |
| --- |


|  |
| --- |


<!-- Page 3 -->
<div class="image-container">
<img src="images/LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn_page_3_img_1.png" alt="Image from page 3">
</div>

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### Step 1: Configure Your Application

#### 1. Select your application in the LinkedIn Developer Portal .

#### 2. Click the Auth tab to view your application credentials.

3. Add the redirect (callback) URL via HTTPS to your server.

#### ７ Note

LinkedIn servers will only communicate with URLs that you have identified as trusted.

#### URLs must be absolute:

#### https://dev.example.com/auth/linkedin/callback

#### not /auth/linkedin/callback

#### parameters are ignored:

#### https://dev.example.com/auth/linkedin/callback?id=1

#### will be https://dev.example.com/auth/linkedin/callback

#### URLs cannot include a #

#### https://dev.example.com/auth/linkedin/callback#linkedin is invalid.

If you are using Postman to test this flow, use https://oauth.pstmn.io/v1/callback as your

#### redirect URL and enable Authorize using browser.

Each application is assigned a unique Client ID (Consumer key/API key) and Client Secret.

Please make a note of these values as they will be integrated into your application. Your Client

Secret protects your application's security so be sure to keep it secure!

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 3 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| Step 1: Configure Your Application
1. Select your application in the LinkedIn Developer Portal .
2. Click the Auth tab to view your application credentials.
3. Add the redirect (callback) URL via HTTPS to your server.
７ Note
LinkedIn servers will only communicate with URLs that you have identified as trusted.
URLs must be absolute:
https://dev.example.com/auth/linkedin/callback
not /auth/linkedin/callback
parameters are ignored:
https://dev.example.com/auth/linkedin/callback?id=1
will be https://dev.example.com/auth/linkedin/callback
URLs cannot include a #
https://dev.example.com/auth/linkedin/callback#linkedin is invalid.
If you are using Postman to test this flow, use https://oauth.pstmn.io/v1/callback as your
redirect URL and enable Authorize using browser.
Each application is assigned a unique Client ID (Consumer key/API key) and Client Secret.
Please make a note of these values as they will be integrated into your application. Your Client
Secret protects your application's security so be sure to keep it secure! |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 3 of 14 |


|  |
| --- |


<!-- Page 4 -->
<div class="image-container">
<img src="images/LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn_page_4_img_1.png" alt="Image from page 4">
</div>

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### ２ Warning

Do not share your Client Secret value with anyone, and do not pass it in the URL when

making API calls, or URI query-string parameters, or post in support forums, chat, etc.

#### Step 2: Request an Authorization Code

To request an authorization code, you must direct the member's browser to LinkedIn's OAuth

2.0 authorization page, where the member either accepts or denies your application's

#### permission request.

#### Once the request is made, one of the following occurs:

1. If it is a first-time request, the permission request timed out, or was manually revoked by

the member: the browser is redirected to LinkedIn's authorization consent window.

2. If there is an existing permission grant from the member: the authorization screen is

bypassed and the member is immediately redirected to the URL provided in the

#### redirect_uri query parameter.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 4 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| ２ Warning
Do not share your Client Secret value with anyone, and do not pass it in the URL when
making API calls, or URI query-string parameters, or post in support forums, chat, etc.
Step 2: Request an Authorization Code
To request an authorization code, you must direct the member's browser to LinkedIn's OAuth
2.0 authorization page, where the member either accepts or denies your application's
permission request.
Once the request is made, one of the following occurs:
1. If it is a first-time request, the permission request timed out, or was manually revoked by
the member: the browser is redirected to LinkedIn's authorization consent window.
2. If there is an existing permission grant from the member: the authorization screen is
bypassed and the member is immediately redirected to the URL provided in the
redirect_uri query parameter. |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 4 of 14 |


<!-- Page 5 -->
<div class="image-container">
<img src="images/LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn_page_5_img_1.png" alt="Image from page 5">
</div>

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

When the member completes the authorization process, the browser is redirected to the URL

#### provided in the redirect_uri query parameter.

#### ７ Note

If the scope permissions are changed in your app, your users must re-authenticate to

ensure that they have explicitly granted your application all of the permissions that it is

#### requesting on their behalf.

#### https

#### GET https://www.linkedin.com/oauth/v2/authorization

#### ﾉ Expand table

#### Parameter Type Description Required

response_type string The value of this field should always be: code Yes

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 5 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| When the member completes the authorization process, the browser is redirected to the URL
provided in the redirect_uri query parameter.
７ Note
If the scope permissions are changed in your app, your users must re-authenticate to
ensure that they have explicitly granted your application all of the permissions that it is
requesting on their behalf.
https
GET https://www.linkedin.com/oauth/v2/authorization
ﾉ Expand table
Parameter Type Description Required
response_type string The value of this field should always be: code Yes |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 5 of 14 |


| https |
| --- |
| GET https://www.linkedin.com/oauth/v2/authorization |


| Parameter Type Description Required |
| --- |
| response_type string The value of this field should always be: code Yes |


<!-- Page 6 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

client_id string The API Key value generated when you registered your application. Yes

redirect_uri url The URI your users are sent back to after authorization. This value Yes

must match one of the Redirect URLs defined in your application

#### configuration . For example,

#### https://dev.example.com/auth/linkedin/callback.

state string A unique string value of your choice that is hard to guess. Used to No

#### prevent CSRF . For example, state=DCEeFWf45A53sdfKef424.

#### scope string URL-encoded, space-delimited list of member permissions your Yes

application is requesting on behalf of the user. These must be

#### explicitly requested. For example,

#### scope=liteprofile%20emailaddress%20w_member_social. See

#### Permissions and Best Practices for Application Development for

#### additional information.

The scopes available to your app depend on which Products or Partner Programs your app has

access to. This information is available in the Developer Portal . Your app's Auth tab will show

current scopes available. You can apply for new Products under the Products tab. If approved,

#### your app will have access to new scopes.

#### Sample Request

#### https

#### GET https://www.linkedin.com/oauth/v2/authorization?response_‐

#### type=code&client_id={your_client_id}&redirect_uri={your_call‐

#### back_url}&state=foobar&scope=liteprofile%20emailaddress%20w_member_social

Once redirected, the member is presented with LinkedIn's authentication screen. This identifies

your application and outlines the particular member permissions/scopes that your application

is requesting. You can change the logo and application name in the Developer Portal under My

#### apps > Settings

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 6 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| client_id string The API Key value generated when you registered your application. Yes
redirect_uri url The URI your users are sent back to after authorization. This value Yes
must match one of the Redirect URLs defined in your application
configuration . For example,
https://dev.example.com/auth/linkedin/callback.
state string A unique string value of your choice that is hard to guess. Used to No
prevent CSRF . For example, state=DCEeFWf45A53sdfKef424.
scope string URL-encoded, space-delimited list of member permissions your Yes
application is requesting on behalf of the user. These must be
explicitly requested. For example,
scope=liteprofile%20emailaddress%20w_member_social. See
Permissions and Best Practices for Application Development for
additional information.
The scopes available to your app depend on which Products or Partner Programs your app has
access to. This information is available in the Developer Portal . Your app's Auth tab will show
current scopes available. You can apply for new Products under the Products tab. If approved,
your app will have access to new scopes.
Sample Request
https
GET https://www.linkedin.com/oauth/v2/authorization?response_‐
type=code&client_id={your_client_id}&redirect_uri={your_call‐
back_url}&state=foobar&scope=liteprofile%20emailaddress%20w_member_social
Once redirected, the member is presented with LinkedIn's authentication screen. This identifies
your application and outlines the particular member permissions/scopes that your application
is requesting. You can change the logo and application name in the Developer Portal under My
apps > Settings |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 6 of 14 |


| dIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1: |
| --- |
| client_id string The API Key value generated when you registered your application. Yes |
| redirect_uri url The URI your users are sent back to after authorization. This value Yes
must match one of the Redirect URLs defined in your application
configuration . For example,
https://dev.example.com/auth/linkedin/callback. |
| state string A unique string value of your choice that is hard to guess. Used to No
prevent CSRF . For example, state=DCEeFWf45A53sdfKef424. |
| scope string URL-encoded, space-delimited list of member permissions your Yes
application is requesting on behalf of the user. These must be
explicitly requested. For example,
scope=liteprofile%20emailaddress%20w_member_social. See
Permissions and Best Practices for Application Development for
additional information. |


|  |
| --- |


|  |
| --- |


|  |
| --- |


| https |
| --- |
| GET https://www.linkedin.com/oauth/v2/authorization?response_‐
type=code&client_id={your_client_id}&redirect_uri={your_call‐
back_url}&state=foobar&scope=liteprofile%20emailaddress%20w_member_social |


|  |
| --- |


<!-- Page 7 -->
<div class="image-container">
<img src="images/LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn_page_7_img_1.png" alt="Image from page 7">
</div>

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### Member Approves Request

By providing valid LinkedIn credentials and clicking Allow, the member approves your

application's request to access their member data and interact with LinkedIn on their behalf.

This approval instructs LinkedIn to redirect the member to the redirect URL that you defined in

#### your redirect_uriparameter.

#### https

#### https://dev.example.com/auth/linkedin/callback?state=foo‐

#### bar&code=AQTQmah11lalyH65DAIivsjsAQV5P-1VTVVebnLl_SCiyMXoIjDmJ4s6rO1VBG‐

#### P5Hx2542KaR_eNawkrWiCiAGxIaV-TCK-mkxDISDak08tdaBzgUYfnTJL1fHRoDWCc‐

#### C2L6LXBCR_z2XHzeWSuqTkR1_jO8CeV9E_WshsJBgE-PWElyvsmfuEXLQbCLfj8CHasuLafFpG‐

#### b0glO4d7M

Attached to the redirect_uri are two important URL arguments that you need to read from

#### the request:

#### code -- The OAuth 2.0 authorization code.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 7 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| Member Approves Request
By providing valid LinkedIn credentials and clicking Allow, the member approves your
application's request to access their member data and interact with LinkedIn on their behalf.
This approval instructs LinkedIn to redirect the member to the redirect URL that you defined in
your redirect_uriparameter.
https
https://dev.example.com/auth/linkedin/callback?state=foo‐
bar&code=AQTQmah11lalyH65DAIivsjsAQV5P-1VTVVebnLl_SCiyMXoIjDmJ4s6rO1VBG‐
P5Hx2542KaR_eNawkrWiCiAGxIaV-TCK-mkxDISDak08tdaBzgUYfnTJL1fHRoDWCc‐
C2L6LXBCR_z2XHzeWSuqTkR1_jO8CeV9E_WshsJBgE-PWElyvsmfuEXLQbCLfj8CHasuLafFpG‐
b0glO4d7M
Attached to the redirect_uri are two important URL arguments that you need to read from
the request:
code -- The OAuth 2.0 authorization code. |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 7 of 14 |


| https |
| --- |
| https://dev.example.com/auth/linkedin/callback?state=foo‐
bar&code=AQTQmah11lalyH65DAIivsjsAQV5P-1VTVVebnLl_SCiyMXoIjDmJ4s6rO1VBG‐
P5Hx2542KaR_eNawkrWiCiAGxIaV-TCK-mkxDISDak08tdaBzgUYfnTJL1fHRoDWCc‐
C2L6LXBCR_z2XHzeWSuqTkR1_jO8CeV9E_WshsJBgE-PWElyvsmfuEXLQbCLfj8CHasuLafFpG‐
b0glO4d7M |


<!-- Page 8 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

state -- A value used to test for possible CSRF attacks.

The code is a value that you exchange with LinkedIn for an OAuth 2.0 access token in the next

step of the authentication process. For security reasons, the authorization code has a 30-

minute lifespan and must be used immediately. If it expires, you must repeat all of the previous

#### steps to request another authorization code.

#### ２ Warning

Before you use the authorization code, your application should ensure that the value

returned in the state parameter matches the state value from your original

authorization code request. This ensures that you are dealing with the real member and

not a malicious script. If the state values do not match, you are likely the victim of a CSRF

attack and your application should return a 401 Unauthorized error code in response.

#### Failed Requests

If the member chooses to cancel, or the request fails for any reason, the client is redirected to

#### your redirect_uri with the following additional query parameters appended:

#### error - A code indicating one of these errors:

user_cancelled_login - The member declined to log in to their LinkedIn account.

#### user_cancelled_authorize - The member refused to authorize the permissions

#### request from your application.

#### error_description - A URL-encoded textual description that summarizes the error.

state - A value passed by your application to prevent CSRF attacks.

#### For more error details, refer here

#### Step 3: Exchange Authorization Code for an

#### Access Token

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 8 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| state -- A value used to test for possible CSRF attacks.
The code is a value that you exchange with LinkedIn for an OAuth 2.0 access token in the next
step of the authentication process. For security reasons, the authorization code has a 30-
minute lifespan and must be used immediately. If it expires, you must repeat all of the previous
steps to request another authorization code.
２ Warning
Before you use the authorization code, your application should ensure that the value
returned in the state parameter matches the state value from your original
authorization code request. This ensures that you are dealing with the real member and
not a malicious script. If the state values do not match, you are likely the victim of a CSRF
attack and your application should return a 401 Unauthorized error code in response.
Failed Requests
If the member chooses to cancel, or the request fails for any reason, the client is redirected to
your redirect_uri with the following additional query parameters appended:
error - A code indicating one of these errors:
user_cancelled_login - The member declined to log in to their LinkedIn account.
user_cancelled_authorize - The member refused to authorize the permissions
request from your application.
error_description - A URL-encoded textual description that summarizes the error.
state - A value passed by your application to prevent CSRF attacks.
For more error details, refer here
Step 3: Exchange Authorization Code for an
Access Token |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 8 of 14 |


|  |
| --- |


|  |
| --- |


|  |
| --- |


<!-- Page 9 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

The next step is to get an access token for your application using the authorization code from

#### the previous step.

#### https

#### POST https://www.linkedin.com/oauth/v2/accessToken

To do this, make the following HTTP POST request with a Content-Type header of x-www-

#### form-urlencoded using the following parameters:

#### ﾉ Expand table

#### Parameter Type Description Required

grant_type string The value of this field should always be: authorization_code Yes

code string The authorization code you received in Step 2. Yes

client_id string The Client ID value generated in Step 1. Yes

client_secret string The Secret Key value generated in Step 1. See the Best Practices Guide Yes

#### for ways to keep your client_secret value secure.

redirect_uri url The same redirect_uri value that you passed in the previous step. Yes

#### Sample Request

#### https

#### https

#### POST https://www.linkedin.com/oauth/v2/accessToken

#### Content-Type: application/x-www-form-urlencoded

#### grant_type=authorization_code

#### code={authorization_code_from_step2_response}

#### client_id={your_client_id}

#### client_secret={your_client_secret}

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 9 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| The next step is to get an access token for your application using the authorization code from
the previous step.
https
POST https://www.linkedin.com/oauth/v2/accessToken
To do this, make the following HTTP POST request with a Content-Type header of x-www-
form-urlencoded using the following parameters:
ﾉ Expand table
Parameter Type Description Required
grant_type string The value of this field should always be: authorization_code Yes
code string The authorization code you received in Step 2. Yes
client_id string The Client ID value generated in Step 1. Yes
client_secret string The Secret Key value generated in Step 1. See the Best Practices Guide Yes
for ways to keep your client_secret value secure.
redirect_uri url The same redirect_uri value that you passed in the previous step. Yes
Sample Request
https
https
POST https://www.linkedin.com/oauth/v2/accessToken
Content-Type: application/x-www-form-urlencoded
grant_type=authorization_code
code={authorization_code_from_step2_response}
client_id={your_client_id}
client_secret={your_client_secret} |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 9 of 14 |


| https |
| --- |
| POST https://www.linkedin.com/oauth/v2/accessToken |


| Parameter Type Description Required |
| --- |
| grant_type string The value of this field should always be: authorization_code Yes |
| code string The authorization code you received in Step 2. Yes |
| client_id string The Client ID value generated in Step 1. Yes |
| client_secret string The Secret Key value generated in Step 1. See the Best Practices Guide Yes
for ways to keep your client_secret value secure. |
| redirect_uri url The same redirect_uri value that you passed in the previous step. Yes |


|  |
| --- |
| https |
| https
POST https://www.linkedin.com/oauth/v2/accessToken
Content-Type: application/x-www-form-urlencoded
grant_type=authorization_code
code={authorization_code_from_step2_response}
client_id={your_client_id}
client_secret={your_client_secret} |
| //learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 9 |


| https |
| --- |
| POST https://www.linkedin.com/oauth/v2/accessToken
Content-Type: application/x-www-form-urlencoded
grant_type=authorization_code
code={authorization_code_from_step2_response}
client_id={your_client_id}
client_secret={your_client_secret} |
| arn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Pag |


<!-- Page 10 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### redirect_uri={your_callback_url}

#### Response

A successful access token request returns a JSON object containing the following fields:

#### ﾉ Expand table

#### Parameter Type Description

access_token string The access token for the application. This value must be kept secure as

specified in the API Terms of Use . The length of access tokens is

~500 characters. We recommend that you plan for your application to

handle tokens with length of at least 1000 characters to accommodate

any future expansion plans. This applies to both access tokens and

#### refresh tokens.

expires_in int The number of seconds remaining until the token expires. Currently, all

#### access tokens are issued with a 60-day lifespan.

refresh_token string Your refresh token for the application. This token must be kept secure.

refresh_token_expires_in int The number of seconds remaining until the refresh token expires.

#### Refresh tokens usually have a longer lifespan than access tokens.

#### scope string URL-encoded, space-delimited list of member permissions your

#### application has requested on behalf of the user.

#### JSON

#### {

#### "access_token":"AQUvlL_DYEzvT2wz1QJiEPeLioeA",

#### "expires_in":5184000,

#### "scope":"r_basicprofile"

#### }

For more error details, refer to the API Error Details table.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 10 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| redirect_uri={your_callback_url}
Response
A successful access token request returns a JSON object containing the following fields:
ﾉ Expand table
Parameter Type Description
access_token string The access token for the application. This value must be kept secure as
specified in the API Terms of Use . The length of access tokens is
~500 characters. We recommend that you plan for your application to
handle tokens with length of at least 1000 characters to accommodate
any future expansion plans. This applies to both access tokens and
refresh tokens.
expires_in int The number of seconds remaining until the token expires. Currently, all
access tokens are issued with a 60-day lifespan.
refresh_token string Your refresh token for the application. This token must be kept secure.
refresh_token_expires_in int The number of seconds remaining until the refresh token expires.
Refresh tokens usually have a longer lifespan than access tokens.
scope string URL-encoded, space-delimited list of member permissions your
application has requested on behalf of the user.
JSON
{
"access_token":"AQUvlL_DYEzvT2wz1QJiEPeLioeA",
"expires_in":5184000,
"scope":"r_basicprofile"
}
For more error details, refer to the API Error Details table. |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 10 of 14 |


| 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25 |
| --- |
| redirect_uri={your_callback_url} |


|  |
| --- |


| Parameter Type Description |
| --- |
| access_token string The access token for the application. This value must be kept secure as
specified in the API Terms of Use . The length of access tokens is
~500 characters. We recommend that you plan for your application to
handle tokens with length of at least 1000 characters to accommodate
any future expansion plans. This applies to both access tokens and
refresh tokens. |
| expires_in int The number of seconds remaining until the token expires. Currently, all
access tokens are issued with a 60-day lifespan. |
| refresh_token string Your refresh token for the application. This token must be kept secure. |
| refresh_token_expires_in int The number of seconds remaining until the refresh token expires.
Refresh tokens usually have a longer lifespan than access tokens. |
| scope string URL-encoded, space-delimited list of member permissions your
application has requested on behalf of the user. |


|  |
| --- |


| JSON |
| --- |
| {
"access_token":"AQUvlL_DYEzvT2wz1QJiEPeLioeA",
"expires_in":5184000,
"scope":"r_basicprofile"
} |


<!-- Page 11 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### ７ Note

#### Access Token Scopes and Lifetime

Access tokens stay valid until the number of seconds indicated in the expires_in field in

the API response. You can go through the OAuth flow on multiple clients (browsers or

devices) and simultaneously hold multiple valid access tokens if the same scope is

requested. If you request a different scope than the previously granted scope, all the

#### previous access tokens are invalidated.

#### Step 4: Make Authenticated Requests

Once you've obtained an access token, you can start making authenticated API requests on

behalf of the member by including an Authorization header in the HTTP call to LinkedIn's API.

#### Sample Request

#### Bash

#### curl -X GET https://api.linkedin.com/v2/me' \

#### -H 'Authorization: Bearer {INSERT_TOKEN}'

#### Step 5: Refresh Access Token

####  Tip

To protect members' data, LinkedIn does not generate long-lived access tokens.

Make sure your application refreshes access tokens before they expire, to avoid

#### unnecessarily sending your application's users through the authorization process

#### again.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 11 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| ７ Note
Access Token Scopes and Lifetime
Access tokens stay valid until the number of seconds indicated in the expires_in field in
the API response. You can go through the OAuth flow on multiple clients (browsers or
devices) and simultaneously hold multiple valid access tokens if the same scope is
requested. If you request a different scope than the previously granted scope, all the
previous access tokens are invalidated.
Step 4: Make Authenticated Requests
Once you've obtained an access token, you can start making authenticated API requests on
behalf of the member by including an Authorization header in the HTTP call to LinkedIn's API.
Sample Request
Bash
curl -X GET https://api.linkedin.com/v2/me' \
-H 'Authorization: Bearer {INSERT_TOKEN}'
Step 5: Refresh Access Token
 Tip
To protect members' data, LinkedIn does not generate long-lived access tokens.
Make sure your application refreshes access tokens before they expire, to avoid
unnecessarily sending your application's users through the authorization process
again. |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 11 of 14 |


| Bash |
| --- |
| curl -X GET https://api.linkedin.com/v2/me' \
-H 'Authorization: Bearer {INSERT_TOKEN}' |


<!-- Page 12 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

Refreshing an access token is a seamless user experience. To refresh an access token, go

through the authorization process again to fetch a new token. This time however, in the refresh

workflow, the authorization screen is bypassed, and the member is redirected to your redirect

#### URL, provided the following conditions are met:

#### The member is still logged into www.linkedin.com

#### The member's current access token has not expired

If the member is no longer logged in to www.linkedin.com or their access token has expired,

#### they are sent through the normal authorization process.

Programmatic refresh tokens are available for a limited set of partners. If this feature has been

#### enabled for your application, see Programmatic Refresh Tokens for instructions.

#### API Error Details

Following are the API errors and its resolution for 3-legged OAuth. If you wish to view the

standard HTTP status codes and its meaning, see Error Handling page.

#### /oauth/v2/authorization

#### ﾉ Expand table

#### HTTP ERROR ERROR DESCRIPTION RESOLUTION

#### STATUS MESSAGE

#### CODE

401 Redirect_uri Redirect URI passed in the Ensure that the redirect URI passed in the

doesn't request does not match the request match the redirect URI added in the

#### match redirect URI added to the developer application under the

#### developer application. Authorization tab.

401 Client_id Client ID passed in the request Ensure that the client ID passed is in match

doesn't does not match the client ID of with the developer application.

#### match the developer application.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 12 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| Refreshing an access token is a seamless user experience. To refresh an access token, go
through the authorization process again to fetch a new token. This time however, in the refresh
workflow, the authorization screen is bypassed, and the member is redirected to your redirect
URL, provided the following conditions are met:
The member is still logged into www.linkedin.com
The member's current access token has not expired
If the member is no longer logged in to www.linkedin.com or their access token has expired,
they are sent through the normal authorization process.
Programmatic refresh tokens are available for a limited set of partners. If this feature has been
enabled for your application, see Programmatic Refresh Tokens for instructions.
API Error Details
Following are the API errors and its resolution for 3-legged OAuth. If you wish to view the
standard HTTP status codes and its meaning, see Error Handling page.
/oauth/v2/authorization
ﾉ Expand table
HTTP ERROR ERROR DESCRIPTION RESOLUTION
STATUS MESSAGE
CODE
401 Redirect_uri Redirect URI passed in the Ensure that the redirect URI passed in the
doesn't request does not match the request match the redirect URI added in the
match redirect URI added to the developer application under the
developer application. Authorization tab.
401 Client_id Client ID passed in the request Ensure that the client ID passed is in match
doesn't does not match the client ID of with the developer application.
match the developer application. |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 12 of 14 |


|  |
| --- |


|  |
| --- |


| HTTP ERROR ERROR DESCRIPTION RESOLUTION
STATUS MESSAGE
CODE |
| --- |
| 401 Redirect_uri Redirect URI passed in the Ensure that the redirect URI passed in the
doesn't request does not match the request match the redirect URI added in the
match redirect URI added to the developer application under the
developer application. Authorization tab. |
| 401 Client_id Client ID passed in the request Ensure that the client ID passed is in match
doesn't does not match the client ID of with the developer application.
match the developer application. |


<!-- Page 13 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

401 Invalid Permissions passed in the Ensure that the permissions sent in scope

#### scope request is invalid parameter is assigned to the developer

#### application in the developer portal.

#### /oauth/v2/accessToken

#### ﾉ Expand table

#### HTTP ERROR MESSAGE ERROR RESOLUTION

#### STATUS DESCRIPTION

#### CODE

#### 401 invalid_request "Unable to retrieve Authorization Check whether the sent

access token: authorization code not code sent is authorization code is valid.

#### found" invalid or not

#### found.

400 invalid_request "A required parameter Redirect_uri in Pass the redirect_uri in the request

"redirect_uri" is missing" the request is to route user back to correct

#### missing. It is landing page.

#### mandatory

#### parameter.

#### 400 invalid_request "A required parameter Authorization Pass the Authorization code

"code" is missing" code in the received as part of authorization

#### request is API call.

#### missing. It is

#### mandatory

#### parameter.

400 invalid_request "A required parameter Grant type in Add grant_type as

#### "grant_type" is missing" the request is "authorization_code" in the

#### missing. It is request.

#### mandatory

#### parameter.

400 invalid_request "A required parameter Client ID in Pass the client id of the app in

#### "client_id" is missing" the request is request.

#### missing. It is

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 13 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| 401 Invalid Permissions passed in the Ensure that the permissions sent in scope
scope request is invalid parameter is assigned to the developer
application in the developer portal.
/oauth/v2/accessToken
ﾉ Expand table
HTTP ERROR MESSAGE ERROR RESOLUTION
STATUS DESCRIPTION
CODE
401 invalid_request "Unable to retrieve Authorization Check whether the sent
access token: authorization code not code sent is authorization code is valid.
found" invalid or not
found.
400 invalid_request "A required parameter Redirect_uri in Pass the redirect_uri in the request
"redirect_uri" is missing" the request is to route user back to correct
missing. It is landing page.
mandatory
parameter.
400 invalid_request "A required parameter Authorization Pass the Authorization code
"code" is missing" code in the received as part of authorization
request is API call.
missing. It is
mandatory
parameter.
400 invalid_request "A required parameter Grant type in Add grant_type as
"grant_type" is missing" the request is "authorization_code" in the
missing. It is request.
mandatory
parameter.
400 invalid_request "A required parameter Client ID in Pass the client id of the app in
"client_id" is missing" the request is request.
missing. It is |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 13 of 14 |


| dIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1: |
| --- |
| 401 Invalid Permissions passed in the Ensure that the permissions sent in scope
scope request is invalid parameter is assigned to the developer
application in the developer portal. |


| HTTP ERROR MESSAGE ERROR RESOLUTION
STATUS DESCRIPTION
CODE |
| --- |
| 401 invalid_request "Unable to retrieve Authorization Check whether the sent
access token: authorization code not code sent is authorization code is valid.
found" invalid or not
found. |
| 400 invalid_request "A required parameter Redirect_uri in Pass the redirect_uri in the request
"redirect_uri" is missing" the request is to route user back to correct
missing. It is landing page.
mandatory
parameter. |
| 400 invalid_request "A required parameter Authorization Pass the Authorization code
"code" is missing" code in the received as part of authorization
request is API call.
missing. It is
mandatory
parameter. |
| 400 invalid_request "A required parameter Grant type in Add grant_type as
"grant_type" is missing" the request is "authorization_code" in the
missing. It is request.
mandatory
parameter. |
| 400 invalid_request "A required parameter Client ID in Pass the client id of the app in
"client_id" is missing" the request is request.
missing. It is |
| //learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 13 |


<!-- Page 14 -->

LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM

#### mandatory

#### parameter.

400 invalid_request "A required parameter Client Secret Pass the client secret of the app in

#### "client_secret" is missing" in the request request.

#### is missing. It is

#### mandatory

#### parameter.

400 invalid_redirect_uri "Unable to retrieve Invalid Pass the right redirect uri tagged

access token: appid/redirect uri/code redirect uri is to the developer application.

#### verifier does not match authorization passed in the

#### code. Or authorization code expired. Or request.

#### external member binding exists"

#### 400 invalid_redirect_uri "Unable to retrieve Invalid Authorization code expired and

#### access token: appid/redirect uri/code Authorization re-authenticate member to

verifier does not match authorization code is sent as generate new authorization code

code. Or authorization code expired. Or part of the and pass the fresh authorization

#### external member binding exists request" code to exchange for access

#### token.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1 Page 14 of 14


| LinkedIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1:17 PM |
| --- |
| mandatory
parameter.
400 invalid_request "A required parameter Client Secret Pass the client secret of the app in
"client_secret" is missing" in the request request.
is missing. It is
mandatory
parameter.
400 invalid_redirect_uri "Unable to retrieve Invalid Pass the right redirect uri tagged
access token: appid/redirect uri/code redirect uri is to the developer application.
verifier does not match authorization passed in the
code. Or authorization code expired. Or request.
external member binding exists"
400 invalid_redirect_uri "Unable to retrieve Invalid Authorization code expired and
access token: appid/redirect uri/code Authorization re-authenticate member to
verifier does not match authorization code is sent as generate new authorization code
code. Or authorization code expired. Or part of the and pass the fresh authorization
external member binding exists request" code to exchange for access
token. |


| dIn 3-Legged OAuth Flow - LinkedIn | Microsoft Learn 7/27/25, 1: |
| --- |
| mandatory
parameter. |
| 400 invalid_request "A required parameter Client Secret Pass the client secret of the app in
"client_secret" is missing" in the request request.
is missing. It is
mandatory
parameter. |
| 400 invalid_redirect_uri "Unable to retrieve Invalid Pass the right redirect uri tagged
access token: appid/redirect uri/code redirect uri is to the developer application.
verifier does not match authorization passed in the
code. Or authorization code expired. Or request.
external member binding exists" |
| 400 invalid_redirect_uri "Unable to retrieve Invalid Authorization code expired and
access token: appid/redirect uri/code Authorization re-authenticate member to
verifier does not match authorization code is sent as generate new authorization code
code. Or authorization code expired. Or part of the and pass the fresh authorization
external member binding exists request" code to exchange for access
token. |


---

*This document was converted using the Enhanced PDF to Markdown Converter, which preserves layout, styling, and images from the original PDF.*
