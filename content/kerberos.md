Title: How to enable Kerberos Authentication in Google Chrome
Date: 2016-04-22 12:03
Modified: 2016-04-22 12:03
Category: kerberos
Tags: kerberos, google-chrome, auth, Linux, Fedora-22
Slug: krb-auth-chrome
Authors: Abhijeet Kasurde
Summary: This blog post will help you to enable Kerberos Authentication in Google Chrome

Enable Simple and protected GSSAPI Negotiation Mechanism (SPNEGO) in google-chrome for allowing user
to login using Kerberos Authentication used by Base OS

* Firstly, install [Google Chrome](https://www.google.com/chrome/)

* and then create an empty directory

    <pre>$ mkdir -p /etc/opt/chrome/policies/managed/ </pre>

* Now, create a JSON file with following content

    <pre>$ cd /etc/opt/chrome/policies/managed/ </pre>
    <pre>$ cat mydomain.json
    { "AuthServerWhitelist": "*.mydomain.com",
      "AuthNegotiateDelegateWhitelist": "*.mydomain.com" }</pre>

Restart chrome and You are all set.
