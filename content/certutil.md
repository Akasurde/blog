Title: Certutil Command for Linux
Date: 2016-12-11 12:03
Modified: 2016-12-11 12:03
Category: grep
Tags: Certificate commands cheatsheet
Slug: certutil-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Certutil command - Cheatsheet


* View pkcs12 file using keytool

    <pre>$ keytool -list -keystore "PATH_TO_P12_FILE" -storepass "P12_FILE_PASSWORD" -storetype PKCS12 -v</pre>

* Create a new certificate database

    <pre>$ certutil -N -d .</pre>

* List all certificates in a database

    <pre>$ certutil -L -d .</pre>

* List all private keys in a database

    <pre>$ certutil -K -d . -f pwdfile.txt</pre>

* Import the signed certificate into the requesters database

    <pre>$ certutil -A -n "Server-cert" -t ",," -i server.crt -d . </pre>

* To add subject alternative names, use a comma seperated list with the option -8 IE:

    <pre>$ certutil -S -f pwdfile.txt -d . -t ",," -c "Server-Cert" -n "server1" -g 2048 -s "CN=testuser1,O=testrelm.test" </pre>


