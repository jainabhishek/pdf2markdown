
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


# Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn

> **Enhanced Conversion** from PDF: `Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn.pdf`  
> Conversion date: 2025-07-29 19:10:32  
> Pages: 3  
> Images extracted: 0  

---


<!-- Page 1 -->

Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn 7/27/25, 12:47 PM

#### Overview

#### 05/08/2023

The LinkedIn API uses OAuth 2.0 for member (user) authorization and API authentication.

Applications must be authorized and authenticated before they can fetch data from LinkedIn or

#### get access to LinkedIn member data.

#### There are two types of Authorization Flows available:

#### Member Authorization (3-legged OAuth)

#### Application Authorization (2-legged OAuth)

Depending on the type of permissions your integration will require, follow one of the

#### authorization flows to get started.

#### ７ Note

There are several third-party libraries in the open source community which abstract

#### the OAuth 2.0 authentication process in every major programming language.

#### LinkedIn does not support TLS 1.0.

#### Member Authorization (3-legged OAuth

#### Flow)

The Member Authorization grants permissions to your application by a LinkedIn member to

access the member's resources on LinkedIn. Your application has no access to these resources

without member approval. The Member Auth uses the 3-legged OAuth code flow. For step-by-

step instructions on how to implement 3-legged OAuth, see Authorization Code Flow (3-

#### legged OAuth) page.

####  Tip

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fconsumer%2Fcontext Page 1 of 3


| Overview
05/08/2023
The LinkedIn API uses OAuth 2.0 for member (user) authorization and API authentication.
Applications must be authorized and authenticated before they can fetch data from LinkedIn or
get access to LinkedIn member data.
There are two types of Authorization Flows available:
Member Authorization (3-legged OAuth)
Application Authorization (2-legged OAuth)
Depending on the type of permissions your integration will require, follow one of the
authorization flows to get started.
７ Note
There are several third-party libraries in the open source community which abstract
the OAuth 2.0 authentication process in every major programming language.
LinkedIn does not support TLS 1.0.
Member Authorization (3-legged OAuth
Flow)
The Member Authorization grants permissions to your application by a LinkedIn member to
access the member's resources on LinkedIn. Your application has no access to these resources
without member approval. The Member Auth uses the 3-legged OAuth code flow. For step-by-
step instructions on how to implement 3-legged OAuth, see Authorization Code Flow (3-
legged OAuth) page.
 Tip |
| --- |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fconsumer%2Fcontext Page 1 of 3 |


|  |
| --- |


<!-- Page 2 -->

Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn 7/27/25, 12:47 PM

#### When to use 3-legged OAuth

Use this flow if you are requesting access to a member's account to use their data and

make requests on their behalf. This is the most commonly used permission type across

LinkedIn APIs. Open permissions available to all applications are of this type such as

#### r_liteprofile, r_emailaddress, and w_member_social.

#### Member Auth Permissions

Member Authorization Permissions are granted by a LinkedIn member to access members

resources on LinkedIn. Permissions are authorization consents to access LinkedIn resources.

The LinkedIn platform uses permissions to protect and prevent abuse of member data. Your

application must have the appropriate permissions before it can access data. To see the list of

permissions, descriptions and access details, refer to Getting Access to LinkedIn APIs page.

#### Application Authorization (2-legged OAuth

#### Client Credential Flow)

Application Authorization or using 2-Legged OAuth grants permissions to your application to

access protected LinkedIn resources. If you are accessing APIs that are not member specific,

use this flow. Not all APIs support Application Authorization. For example, Marketing APIs you

must use Member Authorization explained above. For step-by-step instructions on how to

#### implement 2-legged OAuth, see Client Credential Flow (2-legged OAuth) page.

#### ７ Note

Always request the minimal permission scopes necessary for your use case.

#### Application Auth Permissions

Application Authorization Permissions are granted to applications to access LinkedIn protected

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fconsumer%2Fcontext Page 2 of 3


| Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn 7/27/25, 12:47 PM |
| --- |
| When to use 3-legged OAuth
Use this flow if you are requesting access to a member's account to use their data and
make requests on their behalf. This is the most commonly used permission type across
LinkedIn APIs. Open permissions available to all applications are of this type such as
r_liteprofile, r_emailaddress, and w_member_social.
Member Auth Permissions
Member Authorization Permissions are granted by a LinkedIn member to access members
resources on LinkedIn. Permissions are authorization consents to access LinkedIn resources.
The LinkedIn platform uses permissions to protect and prevent abuse of member data. Your
application must have the appropriate permissions before it can access data. To see the list of
permissions, descriptions and access details, refer to Getting Access to LinkedIn APIs page.
Application Authorization (2-legged OAuth
Client Credential Flow)
Application Authorization or using 2-Legged OAuth grants permissions to your application to
access protected LinkedIn resources. If you are accessing APIs that are not member specific,
use this flow. Not all APIs support Application Authorization. For example, Marketing APIs you
must use Member Authorization explained above. For step-by-step instructions on how to
implement 2-legged OAuth, see Client Credential Flow (2-legged OAuth) page.
７ Note
Always request the minimal permission scopes necessary for your use case.
Application Auth Permissions
Application Authorization Permissions are granted to applications to access LinkedIn protected |
| https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fconsumer%2Fcontext Page 2 of 3 |


<!-- Page 3 -->

Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn 7/27/25, 12:47 PM

resources. To see the list of permissions, descriptions and access details, refer to Getting Access

#### to LinkedIn APIs page.

#### Sample Application

You can explore the OAuth Sample Applications that enables you to try out RESTful OAuth calls

to the LinkedIn Authentication server. The sample app is available in Java.

#### Additionally, you can also explore the Marketing Sample Application.

#### https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fconsumer%2Fcontext Page 3 of 3


| Authenticating with OAuth 2.0 Overview - LinkedIn | Microsoft Learn 7/27/25, 12:47 PM |
| --- |
| resources. To see the list of permissions, descriptions and access details, refer to Getting Access
to LinkedIn APIs page.
Sample Application
You can explore the OAuth Sample Applications that enables you to try out RESTful OAuth calls
to the LinkedIn Authentication server. The sample app is available in Java.
Additionally, you can also explore the Marketing Sample Application. |


---

*This document was converted using the Enhanced PDF to Markdown Converter, which preserves layout, styling, and images from the original PDF.*
