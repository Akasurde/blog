Title: The missing manual - mod-nss
Date: 2017-01-13 12:03
Modified: 2017-01-13 12:03
Category: mod-nss
Tags: mod-nss
Slug: mod-nss-the-missing-manual
Authors: Abhijeet Kasurde
Summary: The missing manual - mod-nss

mod_nss
=======

Introduction
-------------


The mod_ssl package was created in April 1998 by Ralf S. Engelschall and was originally derived from the Apache-SSL package developed by Ben Laurie. It is licensed under the Apache 2.0 license.

**mod_nss** is based directly on the mod_ssl package from Apache 2.0.54. It is a conversion from using OpenSSL calls to using NSS calls instead.

Building
--------

Refer to the README file included with the distribution.

To build you'll need NSPR 4.4.1 or above and NSS 3.9.2 or above. It may work with earlier versions but these are recommended (or tested). These can be retrieved from [Mozilla](http://www.mozilla.org/). The `--with-nspr` and `--with-nss` options require that the package be installed in the same parent directory (e.g. `/opt/nspr`, `/usr/local/nspr`, etc). It will look in this parent for include/ and lib/, etc.

To build with ECC support you need NSPR 4.6.2 or higher and NSS 3.11.2 or higher.

You will also need the NSS and NSPR directories in your library search path (either /etc/ld.so.conf or LD_LIBRARY_PATH) to link and run the module.


Run the configure script. The following mod_nss-specific options are available:

 Option | Description
 ------ | -----------
--with-nss=[PATH] | The file system path to the NSS installation. The assumption is that this has the layout of: PATH/lib, PATH/include, etc.
--with-nss-inc=PATH | The file system path to the NSS include directory (e.g. /usr/local/include/nss3)
--with-nss-lib=PATH | The file system path to the NSS lib directory (e.g. /usr/local/lib)
--with-nspr=[PATH] | The file system path of the NSPR installation. The assumption is that this has the layout of: PATH/lib, PATH/include, etc.
--with-nspr-inc=PATH | The file system path to the NSPR include directory (e.g. /usr/local/include/nspr4)
--with-nspr-lib=PATH | The file system path to the NSPR lib directory (e.g. /usr/local/lib)
--with-apxs=[PATH] | The location of the apxs binary of the Apache you want to install the module into.
--with-apr-config=[PATH] | The location of apr-config which tells us where the APR include files and libraries are located
--enable-ecc | Enable Elliptical Curve Cryptography. Disabled by default.

If `--with-nss` or `--with-nspr` are not passed configure will look for the `[nss|nspr]-devel` packages and use the libraries with that if found.

It is strongly recommended that the mozilla.org version be used.

Build and install those packages somewhere then configure the module with something like:

  <pre>
  % ./configure --with-apxs=/path/to/apxs/ --with-nspr=/path/to/nspr/ --with-nss=/path/to/nss/
  % gmake</pre>

This will create a sample configuration file nss.conf. By default this is installed during the installation process.

Installation
-------------


The make install target uses apxs to install the module into Apache.

This automatically copies the mod_nss shared library to the appropriate location and updates Apache's httpd.conf so that the module will be loaded during the next restart.

It also tries to rename ssl.conf to ssl.conf.old.

The assumption is that mod_nss is replacing mod_ssl. They can co-exist as long as they are listening on separate ports.

The mod_nss configuration file, nss.conf, is copied into the Apache configuration directory (as reported by apxs). You may need to make a manual change to httpd.conf to load this file. If you have a Red Hat-style Apache installation with a conf.d just move `nss.conf` there. It will be automatically loaded. Otherwise you will need to add the following line to `httpd.conf` (location relative to `httpd.conf`):

    Include conf/nss.conf

This has Apache load the `mod_nss` configuration file, `nss.conf`. It is here that you will setup your VirtualServer entries to and configure your SSL servers. If you have a certificate with Subject Alternative Names then you can configure separate VirtualServer entries for eacon one.
Certificate Generation

A ksh script, `gencert`, is included to automatically generate a self-signed CA plus one server certificate. This is fine for testing purposes but it is strongly recommended that a real server certificate be obtained from a real CA before moving a `mod_nss` server into production. Users should be expected to cancel any request to a secure server signed by an unknown issuer.

`gencert` takes one argument, the path to the location of the certificate database. A fair amount of output is generated so you can follow what is going on. For the most part most don't need to bother with the details.

The certificate database password is httptest.

A sample run is:
<pre>
  # mkdir /etc/httpd/nss
  # ./gencert /etc/httpd/nss

  #####################################################################
  Generating new server certificate and key database. The password
  is httptest
  #####################################################################

  #####################################################################
  Generating self-signed client CA certificate
  #####################################################################

  Generating key.  This may take a few moments...

  [ Lots of output removed ]
</pre>


You should now have the following files:

  - /etc/httpd/nss/cert8.db
  - /etc/httpd/nss/key3.db
  - /etc/httpd/nss/secmod.db

These 3 files make up an NSS certificate database.

If you have a sql: prefix on the path, like `sql:/etc/httpd/nss`, then it will generate an SQLite NSS database consisting of the following files:

  - /etc/httpd/nss/cert9.db
  - /etc/httpd/nss/key4.db
  - /etc/httpd/nss/pkcs11.txt


Server Startup
--------------

Starting a `mod_nss` server is no different than starting a `mod_ssl` server. You will need to authenticate yourself to the security token (e.g. enter the key password). The sample `nss.conf` is not included in an <IfDefine SSL> so you do not need to use the startssl argument with apachectl.

A sample startup might look like:

  <pre> % apachectl start
  Please enter password for "internal" token:
  </pre>

If you have additional hardware tokens you will be prompted for each token password.

All other output will be written to the Apache log files.

To avoid being prompted for a startup password you can either:

 - Use a password file that contains your token passwords. See NSSPassPhraseDialog for details.

 - Exec a program which provides the token password (either by asking the user or other means. Change the internal token password to a blank with:

   <pre> % modutil -dbdir /path/to/database/directory -changepw "NSS Certificate DB" </pre>

Enter the old password then press Enter twice for the new password to blank it out.


Migration
---------

A perl script, `migrate.pl`, is included to help migrate an existing `mod_ssl` configuration to work with `mod_nss`. There is one optional argument, `-c`, that will try to convert your existing server and CA certificates plus any certificate revocation lists (CRLs) into an NSS certificate database.

The migration script assumes that you are migrating from `ssl.conf` to `nss.conf`. The original file is not changed. All comments, spacing and other directives are maintained so if there is no ssl.conf it is possible to migrate `httpd.conf` to use `mod_nss`. Simply copy `httpd.conf` to `ssl.conf`, run the update, then copy `nss.conf` to `httpd.conf` (after making a backup, of course). This multi-step process gives you a chance to verify that the migration was successful.


Configuration Directives
------------------------

The following mod_ssl Directives are not applicable to mod_nss:

- SSLSessionCache
- SSLMutex
- SSLCertificateChainFile
- SSLCARevocationPath
- SSLCARevocationFile
- SSLVerifyDepth
- SSLCryptoDevice

Details
-------

* * *
* NSSPassPhraseDialog

  Authentication is required in order to use the private key in an NSS certificate database. The method of this authentication is specified with the NSSPassPhraseDialog directive. This directive takes one argument specifying the method of authentication:
  builtin
  The user will be prompted to enter the token password for each cryptographic device. This works seemlessly with any hardware tokens used. The default "device" is the internal token provided by the NSS Certificate database itself.

  `file:/path/to/file`

  The token password(s) may be stored in an ASCII text file which is read during startup so the server can start without user intervention. The format of this file is:

  `token:password`

  An example for the internal token is:

  <pre>
  internal:secret12
  exec:/path/to/executable</pre>

  The listed program will be executed. The only argument is the NSS token name to be authenticated. The return value of the program is ignored. Only what is printed on stdout is passed along as the password.

  A trivial example script is:

  <pre>
  #!/bin/sh
  echo "secret123"
  </pre>

  To prompt using systemd (as root):

  <pre>
  #!/bin/sh
  exec /bin/systemd-ask-password "Enter SSL pass phrase for $1: "
  </pre>

  * *Example*

  <pre>
  NSSPassPhraseDialog builtin
  NSSPassPhraseDialog file:/etc/httpd/alias/password.conf
  NSSPassPhraseDialog exec:/usr/libexec/httpd/httpd-ssl-pass-dialog</pre>

* * *

* NSSPassPhraseHelper

  When Apache starts it loads and unloads any modules that aren't built-in twice. It loads them once so it can verify that the configuration is ok and then it unloads them and re-loads them again when the server is actually ready to receive connections. After the first module load Apache closes access to the terminal so there is no way to prompt for the NSS token passwords (it would also be annoying to have to authenticate twice). Because the module is loaded and unloaded the NSS certificate database needs to be loaded and unloaded as well, causing any pins entered during the first load to be lost and causing the server to be unstartable.

  The solution is the PassPhraseHelper. This is a stand-alone program that also opens the NSS certificate database and stores a copy of the encrypted token password entered during the first load of the NSS module. When mod_nss needs to open the certificate database during subsequent reloads it queries the PassPhraseHelper for the token password.

  Example

  <pre>NSSPassPhraseHelper /path/to/nss_pcache</pre>

  * * *

* NSSCertificateDatabase

  Specifies the location of the NSS certificate database to be used. An NSS certificate database consists of 3 files: `cert8.db`, `key3.db` and `secmod.db`. `cert8.db` stores certificates and Certificate Revocation Lists (CRLs), `key3.db` stores keys and `secmod.db` stores information about available PKCS#11 modules.

  This directive specifies a path, not a filename. To use a sqlite NSS database include the prefix sql: in the path.

  Example

  <pre>NSSCertificateDatabase /etc/httpd/conf/nss
  NSSCertificateDatabase sql:/etc/httpd/conf/nss</pre>

* * *

* NSSDBPrefix

  Normally a certificate database consists of 3 files: `cert8.db`, `key3.db` and `secmod.db`. This directive allows you to add a named prefix to the filenames of `cert8.db` and `key3.db` so you can store multiple databases in one directory.

  Example

  <pre> NSSDBPrefix my-prefix-</pre>

  You would then need: `my-prefix-cert8.db`, `my-prefix-key3.db` and `secmod.db`

  In order to work with files with a prefix using the NSS command-line tools use the -P flag.

* * *

* NSSSessionCacheSize

  Specifies the number of SSL sessions that can be cached.

  There is no upper limit.

  The default value is 10000.

  Example

  <pre>NSSSessionCacheSize 10000</pre>

* * *

* NSSSessionCacheTimeout

  Deprecated.

* * *

* NSSSession3CacheTimeout

  Specifies the number of seconds SSLv3 sessions are cached.

  The valid range is 5 - 86400 seconds. A setting outside the valid range is silently constrained.

  The default value is 86400 (24 hours).

  Example

  <pre>NSSSession3CacheTimeout 86400</pre>

* * *

* NSSRandomSeed

  Configures sources to seed the NSS Random Number Generator (RNG) at startup. Currently this only supports seeding the RNG at startup.

  The following sources are available:
  builtin: Combines the current system time, the current process id and a randomly choosen 128-byte extract of the process stack. This is not a particularly strong source of entropy.
  file:/path/to/source: Reads from the specified file. If the number of bytes to read is specified it just reads that amount. Be aware that some operating systems block on /dev/random if not enough entropy is available. This means that the server will wait until that data is available to continue startup. These systems generally offer a non-blocking device as well, /dev/urandom.
  exec:/path/to/program: Executes the given program and takes the stdout of it as the entropy. If the bytes argument is included it reads that many bytes, otherwise it reads until the program exits.

  Example

  <pre>NSSRandomSeed startup builtin
  NSSRandomSeed startup /dev/urandom 512
  NSSRandomSeed startup /usr/bin/makerandom</pre>

* * *

* NSSSkipPermissionCheck

  The NSS database will be checked to ensure that the user configured to run Apache as has owner or group read access to the database configured in NSSCertificateDatabase. This check can be disabled by setting NSSSkipPermissionCheck to on. The default is off

  Example

  <pre>NSSSkipPermissionCheck on</pre>

* * *

* NSSEngine

  Enables or disables the SSL protocol. This is usually used within a VirtualHost tag to enable SSL for a particular virtual host.

  SSL is disabled by default.

  Example

  <pre>NSSEngine on</pre>

* * *

* NSSFIPS

  Enables or disables FIPS 140 mode. This replaces the standard internal PKCS#11 module with a FIPS-enabled one. It also forces the enabled protocols to TLSv1.2, TLSv1.1 and TLSv1.0 and disables all ciphers but the FIPS ones. You may still select which ciphers you would like limited to those that are FIPS-certified. Any non-FIPS that are included in the NSSCipherSuite entry are automatically disabled. The allowable ciphers are (with ecc-enabled set):

  - rsa_3des_sha
  - rsa_aes_128_sha
  - rsa_aes_256_sha
  - aes_128_sha_256
  - aes_256_sha_256
  - rsa_aes_128_gcm_sha_256
  - fips_3des_sha
  - ecdh_ecdsa_3des_sha
  - ecdh_ecdsa_aes_128_sha
  - ecdh_ecdsa_aes_256_sha
  - ecdhe_ecdsa_3des_sha
  - ecdhe_ecdsa_aes_128_sha
  - ecdhe_ecdsa_aes_256_sha
  - ecdh_rsa_3des_sha
  - ecdh_rsa_aes_128_sha
  - ecdh_rsa_aes_256_sha
  - ecdhe_rsa_3des_sha
  - ecdhe_rsa_aes_128_sha
  - ecdhe_rsa_aes_256_sha
  - ecdhe_ecdsa_aes_128_sha_256
  - ecdhe_rsa_aes_128_sha_256
  - ecdhe_ecdsa_aes_128_gcm_sha_256
  - ecdhe_rsa_aes_128_gcm_sha_256

  FIPS is disabled by default.

  Example

  <pre>NSSFIPS on</pre>

* * *

* NSSOCSP

  Enables or disables OCSP (Online Certificate Status Protocol). This allows the server to check the validity of a client certificate before accepting it.

  OCSP is disabled by default.

  Example

  <pre>NSSOCSP on</pre>

* * *

* NSSCipherSuite

There are two options for configuring the available ciphers. mod_nss provides its own cipher list, a space-separated list of the SSL ciphers used, with the prefix + to enable or - to disable, using the Cipher Name value in the tables below.

Alternatively the mod_nss-style cipher definitions may be used, [sslciphersuite](http://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslciphersuite).

The support options are:

- ALL
- COMPLEMENTOFALL
- DEFAULT
- RSA
- EDH
- NULL
- eNULL
- AES
- 3DES
- DES
- RC4,
- MD5
- SHA
- SHA1
- SHA256
- SSLv3
- TLSv1
- TLSv12
- HIGH
- MEDIUM
- LOW
- EXPORT
- EXPORT40
- EXPORT56

If a cipher string value contains a colon it is considered a mod_ssl-style cipher string.

If a cipher string value contains a comma it is considered a mod_nss-style cipher string.

If it contains neither then mod_nss first tries to apply OpenSSL ciphers then NSS ciphers.

All ciphers are disabled by default.

Available RSA ciphers are:


Cipher Name  |  NSS Cipher definition   |  Protocol
------------ | ------------------------ | ----------
rsa_3des_sha | TLS_RSA_WITH_3DES_EDE_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_des_sha | TLS_RSA_WITH_DES_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_null_md5 | TLS_RSA_WITH_NULL_MD5 | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_null_sha | TLS_RSA_WITH_NULL_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_rc2_40_md5 | TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5 | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_rc4_128_md5 | TLS_RSA_WITH_RC4_128_MD5 | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_rc4_128_sha | TLS_RSA_WITH_RC4_128_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_rc4_40_md5 | TLS_RSA_EXPORT_WITH_RC4_40_MD5 | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
fips_des_sha | SSL_RSA_FIPS_WITH_DES_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
fips_3des_sha | SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_des_56_sha | TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_rc4_56_sha | TLS_RSA_EXPORT1024_WITH_RC4_56_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_aes_128_sha | TLS_RSA_WITH_AES_128_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
rsa_aes_256_sha | TLS_RSA_WITH_AES_256_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
camelia_128_sha | TLS_RSA_WITH_CAMELLIA_128_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
camelia_256_sha | TLS_RSA_WITH_CAMELLIA_256_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
null_sha_256 | TLS_RSA_WITH_NULL_SHA256 | TLSv1.2
aes_128_sha_256 | TLS_RSA_WITH_AES_128_CBC_SHA256 | TLSv1.2
aes_256_sha_256 | TLS_RSA_WITH_AES_256_CBC_SHA256 | TLSv1.2
rsa_aes_128_gcm_sha_256 | TLS_RSA_WITH_AES_128_GCM_SHA256 | TLSv1.2

The available server-side DHE ciphers are:

Cipher Name | NSS Cipher definition | Protocol
----------- | --------------------- | --------
dhe_rsa_des_sha | TLS_DHE_RSA_WITH_DES_CBC_SHA | SSLv3/TLSv1.0/TLSv1.1/TLSv1.2
dhe_rsa_3des_sha | TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
dhe_rsa_aes_128_sha | TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
dhe_rsa_aes_256_sha | TLS_DHE_RSA_WITH_AES_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
dhe_rsa_camellia_128_sha | TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
dhe_rsa_camellia_256_sha | TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
dhe_rsa_aes_128_sha256 | TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 | TLSv1.2
dhe_rsa_aes_256_sha256 | TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 | TLSv1.2
dhe_rsa_aes_128_gcm_sha_256 | TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 | TLSv1.2


Additionally there are a number of ECC ciphers:

Cipher Name | NSS Cipher definition | Protocol
----------- | --------------------- | --------
ecdh_ecdsa_null_sha | TLS_ECDH_ECDSA_WITH_NULL_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_ecdsa_rc4_128_sha | TLS_ECDH_ECDSA_WITH_RC4_128_SHA |  TLSv1.0/TLSv1.1/TLSv1.2
ecdh_ecdsa_3des_sha | TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_ecdsa_aes_128_sha |  TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_ecdsa_aes_256_sha | TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_ecdsa_null_sha | TLS_ECDHE_ECDSA_WITH_NULL_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_ecdsa_rc4_128_sha | TLS_ECDHE_ECDSA_WITH_RC4_128_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_ecdsa_3des_sha | TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_ecdsa_aes_128_sha | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_ecdsa_aes_256_sha | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_rsa_null_sha | TLS_ECDH_RSA_WITH_NULL_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_rsa_128_sha | TLS_ECDH_RSA_WITH_RC4_128_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_rsa_3des_sha | TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_rsa_aes_128_sha | TLS_ECDH_RSA_WITH_AES_128_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_rsa_aes_256_sha | TLS_ECDH_RSA_WITH_AES_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
echde_rsa_null | TLS_ECDHE_RSA_WITH_NULL_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_rsa_rc4_128_sha | TLS_ECDHE_RSA_WITH_RC4_128_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_rsa_3des_sha | TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_rsa_aes_128_sha | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_rsa_aes_256_sha | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_anon_null_sha | TLS_ECDH_anon_WITH_NULL_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_anon_rc4_128sha | TLS_ECDH_anon_WITH_RC4_128_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_anon_3des_sha | TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_anon_aes_128_sha | TLS_ECDH_anon_WITH_AES_128_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdh_anon_aes_256_sha | TLS_ECDH_anon_WITH_AES_256_CBC_SHA | TLSv1.0/TLSv1.1/TLSv1.2
ecdhe_ecdsa_aes_128_sha_256 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | TLSv1.2
ecdhe_rsa_aes_128_sha_256  | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | TLSv1.2
ecdhe_ecdsa_aes_128_gcm_sha_256 | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | TLSv1.2
ecdhe_rsa_aes_128_gcm_sha_256 | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | TLSv1.2


  Example

  <pre>NSSCipherSuite +rsa_3des_sha,-rsa_des_56_sha,+rsa_des_sha,-rsa_null_md5,-rsa_null_sha,-rsa_rc2_40_md5,+rsa_rc4_128_md5,-rsa_rc4_128_sha,-rsa_rc4_40_md5,-rsa_rc4_56_sha,-fips_des_sha, +fips_3des_sha,-rsa_aes_128_sha,-rsa_aes_256_sha
NSSCipherSuite ALL
NSSCipherSuite rsa_3des_sha
NSSCipherSuite RC4-SHA</pre>

* * *

* NSSProtocol

  A comma-separated string that lists the basic protocols that the server can use (and clients may connect with). It doesn't enable a cipher specifically but allows ciphers for that protocol to be used at all.

  Options are:

  - SSLv3
  - TLSv1 (legacy only; replaced by TLSv1.0)
  - TLSv1.0
  - TLSv1.1
  - TLSv1.2
  - All

  Note that this differs from mod_ssl in that you can't add or subtract protocols.

  If no NSSProtocol is specified, mod_nss will default to allowing the use of the TLSv1.0, TLSv1.1 and TLSv1.2 protocols, where TLSv1.0 will be set to be the minimum protocol allowed, and TLSv1.2 will be set to be the maximum protocol allowed.
  If values for NSSProtocol are specified, mod_nss will set both the minimum and the maximum allowed protocols based upon these entries allowing for the inclusion of every protocol in-between. For example, if only SSLv3 and TLSv1.1 are specified, SSLv3, TLSv1.0, and TLSv1.1 will all be allowed, as NSS utilizes protocol ranges to accept all protocols inclusively (TLSv1.1 -> TLSv1.0 -> SSLv3.0), and does not allow exclusion of any protocols in the middle of a range (e. g. - TLSv1.0).

  Finally, NSS will always automatically negotiate the use of the strongest possible protocol that has been specified which is acceptable to both sides of a given connection.
  SSLv2 is not supported by default at this time.

  Example

  <pre>NSSProtocol SSLv3,TLSv1.0,TLSv1.1</pre>

* * *

* NSSNickname

  Specify the nickname to be used for this the server certificate. Certificates stored in an NSS database are referred to using nicknames which makes accessing a specific certificate much easier. It is also possible to specify the certificate DN but it is easier to use a nickname. If the nickname includes spaces then the value needs to be enclosed in double quotes.

  Example

  <pre>NSSNickname Server-Cert
NSSNickname "This contains a space"</pre>


  **NOTE**: There is nothing magical about the string "Server-Cert." A nickname can be anything. Historically this was Server-Cert in the Netscape server products that used NSS.

* * *

* NSSECCNickname

  Similar to NSSNickname but designed for use with ECC certificates. This allows you to have both an RSA certificate and an ECC certificate available on the same listening port. This allows newer clients that support ECC to connect with those ciphers but also allows older clients to connect with an RSA cipher.

  Example

  NSSNickname Server-Cert-ECC


* * *

* NSSEnforceValidCerts

  By default mod_nss will not start up if the server certificate is not valid. This means that if the certificate has expired or is signed by a CA that is not trusted in the NSS certificate database the server will not start. If you would like the server to start anyway you can add this directive to nss.conf and the server will start with just a warning. Not enforcing a valid server certificate is not recommended.

  Example

  <pre>NSSEnforceValidCerts on</pre>

* * *

* NSSVerifyClient

  Determines whether Client Certificate Authentication will be requested or required. This may be set in a per-server or per-directory context. At the server level the certificate is requested during the initial SSL handshake. In the per-directry context an SSL renogitation is required and a certificate requested from the client.

  Available options are:

  - none: no client certificate is required or requested
  - optional: a client certificate is requested but if one is not available, the connection may continue.
  - require: a valid client certificate is required for the connection to continue.

  The mod_ssl option option_no_ca is not supported.

  There is no NSSVerifyDepth directive. NSS always verifies the entire certificate chain.

  Example

  <pre>NSSVerifyClient require</pre>

* * *

* NSSSessionTickets

  Enables or disables support for TLS Session tickets (RFC 5077). The default is off.

  Example

  <pre>NSSSessionTickets on</pre>

* * *

* NSSUserName

  Defines the field in the client certificate which will set the user field in the request. The option FakeBasicAuth (see NSSOptions) must also be set for this to work.

  Example

  <pre>NSSUserName SSL_CLIENT_S_DN_UID</pre>

* * *

* NSSOptions

  Control various options in a per-server or per-directory context.

  - FakeBasicAuth: When this option is enabled and NSSUserName is set then the certificate attribute defined in NSSUserName is used to populate the value of r->user in the Apache request object. This equates to the environmant variable REMOTE_USER.
  - StdEnvVars: A standard set of SSL environment variables is created.
  CompatEnvVars: A no-op. In previous versions of mod_ssl this would set additional environment variables for backwards compatibility with older Apache SSL implementations.
  - ExportCertData: Several additional environment variables are created, SSL_CLIENT_CERT, SSL_CLIENT_CERT_CHAIN[0..n] and SSL_SERVER_CERT. This provides additional certificate information on the client and server to the environment, plus every CA certificate in the client certificate.
  - StrictRequire: Absolutely forces the connection to be forbidden when NSSRequireSSL or NSSRequire aren't met.
  - OptRenegotiate: Allows the SSL connection to be renegotiated using a different configuration. This is designed for a per-directory and is relatively expensive to do. For example, it can be used to force very strong ciphers in particular directories.

  All options are disabled by default.

  Example:

  <pre>NSSOptions +FakeBasicAuth
  < Files ~ "\.(cgi|shtml)$">
  NSSOptions +StdEnvVars
  < Files></pre>

* * *

* NSSRequireSSL

  The request is forbidden unless the connection is using SSL. Only available in a per-directory context. This takes no arguments.

  Example

  <pre>NSSRequireSSL</pre>

* * *

* NSSRequire

  Provides a regular expression-based access-control mechanism. Access may be restricted (or allowed) based on any number of variables such as components of the client certificate, the remote IP address, etc.

  Example

  <pre>NSSRequire</pre>

* * *

* NSSRenegBufferSize

  Configure the amount of memory that will be used for buffering the request body if a per-location SSL renegotiation is required due to changed access control requirements. The value is in bytes. The default is 128K.
  If set to 0 then no buffering is done.

  Example

  <pre>NSSRenegBufferSize 262144</pre>

* * *

* NSSSNI

  Enables or disables Server Name Identification (SNI) extension check for TLS. This option is enabled by default. To disable SNI, set this to off in the default name-based VirtualHost.

  Example

  <pre>NSSSNI off</pre>

* * *

* NSSStrictSNIVHostCheck

  Configures whether a non-SNI client is allowed to access a name-based VirtualHost. If set to on in the default name-based VirtualHost then clients that are SNI unaware cannot access any virtual host. If set to on in any other VirtualHost then SNI unaware clients cannot access this particular virtual host.

  Example

  <pre>NSSStrictSNIVHostCheck off</pre>

* * *

* NSSProxyEngine

  Enables or disables mod_nss HTTPS support for mod_proxy.

  Example

  <pre>NSSProxyEngine on</pre>

* * *

* NSSProxyProtocol

  Specifies the SSL protocols that may be used in proxy connections. The syntax is identical to NSSProtocol.

  Example

  <pre>NSSProxyProtocol SSLv3</pre>

* * *

* NSSProxyCipherSuite

  Specifies the SSL ciphers available for proxy connections. The syntax is identical to NSSCipherSuite.

  Example

  <pre>NSSProxyCipherSuite +rsa_3des_sha,-rsa_null_md5,-rsa_null_sha,+rsa_rc4_128_md5</pre>

* * *

* NSSProxyNickname

  The nickname of the client certificate to send if the remote server requests client authentication.

  Example

  <pre>NSSProxyNickname beta</pre>

* * *

* NSSProxyCheckPeerCN

  Compare the CN value of the peer certificate with the hostname being requested. If this is set to on, the default, then the request will fail if they do not match. If this is set to off then this comparison is not done. Note that this test is your only protection against a man-in-the-middle attack so leaving this as on is strongly recommended.

  Example

  <pre>NSSProxyCheckPeerCN on</pre>

* * *

Environment Variables
---------------------

Quite a few environment variables (for CGI and SSI) may be set depending on the NSSOptions configuration. It can be expensive to set these so it is recommended that they only be set when they will be used (e.g. don't set them on a per-server basis). Here is a list of the variables along with the option used to set them.

Always Set

Name | Description
----- | ----------
HTTPS | Set to "on" if HTTPS is being used

+StdEnvVars

Name | Description
----- | ----------
SSL_VERSION_INTERFACE | The version of mod_nss the server is running
SSL_VERSION_LIBRARY | The version of NSS that mod_nss was compiled against.
SSL_PROTOCOL | SSLv3, TLSv1.0, TLSv1.1 or TLSv1.2
SSL_CIPHER |  The cipher the connection is using
SSL_CIPHER_EXPORT |  true if the cipher is an export cipher, false otherwise
SSL_CIPHER_USEKEYSIZE | Number if bits the cipher is using
SSL_CIPHER_ALGKEYSIZE | Max number of bits possible in the cipher
SSL_CLIENT_VERIFY | NONE if no client auth, SUCCESS or FAILED if SSLVerifyCert is set
SSL_CLIENT_V_START | Client certificate validity start time
SSL_CLIENT_V_END | Client certificate validity end time
SSL_CLIENT_V_REMAIN | Number of days that the certificate is valid
SSL_CLIENT_M_VERSION | X.509 version of the client certificate
SSL_CLIENT_M_SERIAL | Serial number of the client certificate
SSL_CLIENT_A_KEY  | Algorithm used for client key
SSL_CLIENT_A_SIG  | Algorithm used for the signature of the client key
SSL_CLIENT_S_DN   | Distinguished Name (DN) of the client certificate
SSL_CLIENT_S_DN_[C,ST,L,O,OU,CN,T,I,G,S,D,UID,Email] | Components of the client certificate. Only those that exist in the certificate are created.
SSL_CLIENT_SAN_[DNS, IPAddr, Email, OTHER_msUPN]_[0..n] | A subset of Subject Alternate Names. Each entry is appended with a unique sequential number.
SSL_CLIENT_I_DN |  Distinguished Name (DN) of the client certificate issuer
SSL_CLIENT_I_DN_[C,ST,L,O,OU,CN,T,I,G,S,D,UID,Email]  |  Components of the client issuer certificate. Only those that exist in the certificate are created
SSL_SERVER_DN | Distinguished Name (DN) of the server certificate
SSL_SERVER_DN_[C,ST,L,O,OU,CN,T,I,G,S,D,UID,Email] |   Components of the server certificate. Only those that exist in the certificate are created
SSL_SERVER_I_DN_[C,ST,L,O,OU,CN,T,I,G,S,D,UID,Email] |    Components of the server issuer certificate. Only those that exist in the certificate are created
SSL_SERVER_M_VERSION |  X.509 version of the server certificate
SSL_SERVER_M_SERIAL | Serial number of the server certificate
SSL_SERVER_V_START | Server certificate validity start time
SSL_SERVER_V_END | Server certificate validity end time
SSL_SERVER_A_KEY | Algorithm used for server key
SSL_SERVER_A_SIG | Algorithm used for the signature of the server key
SSL_SESSION_ID |  SSL Session ID
SSL_SERVER_SAN_[DNS, IPAddr, Email, OTHER_msUPN]_[0..n] |    A subset of Subject Alternate Names. Each entry is appended with a unique sequential number.

+ExportCertData

Name | Description
----- | ----------
SSL_SERVER_CERT | The server certificate in PEM format.
SSL_CLIENT_CERT | The client certificate in PEM format (if available)
SSL_CLIENT_CERT_CHAIN_[0..n] | Each certificate in the client certificate chain in PEM format (including the client certificate itself).


Database Management
-------------------

NSS stores it's certificates and keys in a set of files referred to as the "certificate database." The files by default (with NSS 3.x) are named cert8.db, key3.db and secmod.db. See the [NSS documentation](http://www.mozilla.org/projects/security/pki/nss/) for more information on these specific files.
By default the NSS databases use the Berkeley Database format (cert8 and key3). To use the sqlite format (cert9 and key4) either include sql: in all references to the database (-d sql:/path/to/database) or export NSS_DEFAULT_DB_TYPE="sql".

For more details [here](https://wiki.mozilla.org/NSS_Shared_DB)

The NSS database also stores any Certificate Revocation Lists (CRLs).

Several NSS tools are available for managing certificates, keys, PKCS#11 modules and CRLs. These come with the NSS distribution. Here is a brief overview:

Tool | Description
----- | ----------
certutil |  Generate Certificate Signing Requests, install certificates and manage certificate trust flags.
crlutil | Manage certificate revocation lists (CRLs).
modutil | Manage the database of PKCS11 modules (secmod.db). Add modules and modify the properties of existing modules (such as whether a module is the default provider of some crypto service).
pk12util | Import and export keys and certificates in PKCS12 format.


Here are some quick, useful commands. This assumes that the NSPR and NSS libraries are in your LD_LIBRARY_PATH. Certificates may be referred to by either their DN or by a short nickname that is assigned when the certificate is added to the database. The nickname is the preferred method of referring to certificates. All of these commands use the -d option to specify the database location. The default is ~/.netscape and is probably not what you want.

Description | command
----- | ----------
Create a Database |  certutil -N -d [path]
List all Certificates | certutil -L -d [path]
Extract a cert (Server-Cert) in ASCII |  certutil -L -n Server-Cert -d [path] -a
Extract a cert and key (Server-Cert) in PKCS#12 | pk12util -o server.p12 -n Server-Cert -d [path]
Import a cert and key (Import-Me) from PKCS#12 | pk12util -i server.p12 -n Import-Me -d [path]


Importing OpenSSL Certificates
------------------------------

If you have existing OpenSSL certificates you can import them into an NSS certificate database.

To import a server certificate (nickname Server-Cert):

<pre>% openssl pkcs12 -export -in /path/to/certificate -inkey /path/to/keyfile -out server.p12 -name "Server-Cert" -passout pass:foo
% pk12util -i server.p12 -d [path] -W foo </pre>

To import a CA certificate:

<pre>% certutil -A -n "myca" -t "CT,," -d [path] -a -i /path/to/cacertificate</pre>

To import a CRL:

<pre>% openssl crl -in /path/to/crlfile -out /tmp/crl.tmp -inform PEM -outform DER
% crlutil -I -t 1 -d [path] -i /tmp/crl.tmp</pre>

To verify that your server certificate was imported properly, you can have NSS validate it:

<pre>% certutil -V -n Server-Cert -u V -d .
certutil: certificate is valid</pre>
