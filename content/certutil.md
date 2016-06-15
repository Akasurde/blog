Title: Certutil Command for Linux
Date: 2016-06-15 12:03
Modified: 2016-06-15 12:03
Category: grep
Tags: Certificate commands cheatsheet
Slug: certutil-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Certutil command - Cheatsheet


* View pkcs12 file using keytool

    <pre>$ keytool -list -keystore "PATH_TO_P12_FILE" -storepass "P12_FILE_PASSWORD" -storetype PKCS12 -v</pre>
