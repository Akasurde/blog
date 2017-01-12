Title: OpenSSL commands
Date: 2016-12-01 12:03
Modified: 2016-12-01 12:03
Category: certificates
Tags: openssl, cheatsheet
Slug: openssl-cheat-sheet
Authors: Abhijeet Kasurde
Summary: OpenSSL command info


*  Generate a new private key and Certificate Signing Request

    <pre>$ openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key </pre>

* Generate a self-signed certificate

    <pre>$ openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt</pre>

* Generate a certificate signing request (CSR) for an existing private key

    <pre>$ openssl req -out CSR.csr -key privateKey.key -new </pre>

* Generate a certificate signing request based on an existing certificate

    <pre>$ openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key</pre>

* Remove a passphrase from a private key

    <pre>$ openssl rsa -in privateKey.pem -out newPrivateKey.pem</pre>

* Check a Certificate Signing Request (CSR)

    <pre>$ openssl req -text -noout -verify -in CSR.csr</pre>

* Check a private key

    <pre>$ openssl rsa -in privateKey.key -check</pre>

* Check a certificate

    <pre>$ openssl x509 -in certificate.crt -text -noout</pre>

* Check a PKCS#12 file (.pfx or .p12)

    <pre>$ openssl pkcs12 -info -in keyStore.p12</pre>

* Convert a DER file (.crt .cer .der) to PEM

    <pre>$ openssl x509 -inform der -in certificate.cer -out certificate.pem</pre>

* Convert a PEM file to DER

    <pre>$ openssl x509 -outform der -in certificate.pem -out certificate.der</pre>

* Convert a PKCS#12 file (.pfx .p12) containing a private key and certificates to PEM

    <pre>$ openssl pkcs12 -in keyStore.pfx -out keyStore.pem -nodes</pre>

* Convert a PEM certificate file and a private key to PKCS#12 (.pfx .p12)

    <pre>$ openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt</pre>

* Extract Keys from PKCS#12 container

     <pre>$ openssl pkcs12 -in yourP12File.pfx -nocerts -out privateKey.pem </pre>

* Extract Certificates from PKCS#12 container

     <pre>$ openssl pkcs12 -in yourP12File.pfx -clcerts -nokeys -out publicCert.pem </pre>
