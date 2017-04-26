Title: Extract public key from pem and convert to ssh-RSA format
Date: 2017-05-12 12:03
Modified: 2017-05-12 12:03
Category: openssl
Tags: openssl, openssh
Slug: openssl-openssh-pem-to-ssh-rsa
Authors: Abhijeet Kasurde
Summary: Extract public key from pem and convert to ssh-rsa format


In order to extract public key from pem and convert to ssh-RSA format, perform following commands


<pre>$ openssl rsa -in PUBLICKEY.pem -pubout > PUBLICKEY.pub</pre>

<pre>$ ssh-keygen -f PUBLICKEY.pub -i -m PKCS8 </pre>
