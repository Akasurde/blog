Title: Using OCSP with Apache and mod_nss on CentOS 7
Date: 2017-01-17 12:03
Modified: 2017-01-17 12:03
Category: System Administration
Tags: OCSP, mod_nss, httpd, CentOS
Slug: ocsp-mod-nss-httpd-centos
Authors: Abhijeet Kasurde
Summary: Using OCSP with Apache and mod_nss on CentOS 7

Following steps will guide you how to configure OCSP with Apache and mod_nss

In this example, we will configure client certificate authentication using mod_nss and OCSP.

For this setup, we will use two servers

- cybertron.testrelm.test
- tiger.testrelm.test

`cybertron` will be [FreeIPA server](http://www.freeipa.org/page/Main_Page) and `tiger` will be httpd server.

Let us get started -

Installing FreeIPA server on `cybertron`
----------------------------------------

FreeIPA provides `OCSP` server, so we will install and configure FreeIPA server.

<pre>[root@cybertron ~]# yum install -y ipa-server ipa-server-dns
[root@cybertron ~]# ipa-server-install --ip-address $(ip addr|grep "global"|cut -d " " -f6|cut -d "/" -f1|head -n 1) -r testrelm.test -p 'Secret123' -a 'Secret123' --setup-dns --forwarder 192.168.12.255 -U

The log file for this installation can be found in /var/log/ipaserver-install.log
==============================================================================
This program will set up the IPA Server.

This includes:
  * Configure a stand-alone CA (dogtag) for certificate management
  * Configure the Network Time Daemon (ntpd)
  * Create and configure an instance of Directory Server
  * Create and configure a Kerberos Key Distribution Center (KDC)
  * Configure Apache (httpd)
  * Configure DNS (bind)

WARNING: conflicting time&date synchronization service 'chronyd' will be disabled
in favor of ntpd

Warning: skipping DNS resolution of host cybertron.testrelm.test
The domain name has been determined based on the host name.

Checking DNS domain testrelm.test., please wait ...
Checking DNS forwarders, please wait ...

The IPA Master Server will be configured with:
Hostname:       cybertron.testrelm.test
IP address(es): 192.168.12.1
Domain name:    testrelm.test
Realm name:     TESTRELM.TEST

BIND DNS server will be configured to serve IPA domain with:
Forwarders:       192.168.12.255
Forward policy:   only
Reverse zone(s):  No reverse zone

Configuring NTP daemon (ntpd)
  [1/4]: stopping ntpd
  [2/4]: writing configuration
  [3/4]: configuring ntpd to start on boot
  [4/4]: starting ntpd
Done configuring NTP daemon (ntpd).
Configuring directory server (dirsrv). Estimated time: 1 minute
  [1/47]: creating directory server user
  [2/47]: creating directory server instance
  [3/47]: updating configuration in dse.ldif
  [4/47]: restarting directory server
  [5/47]: adding default schema
  [6/47]: enabling memberof plugin
  [7/47]: enabling winsync plugin
  [8/47]: configuring replication version plugin
  [9/47]: enabling IPA enrollment plugin
  [10/47]: enabling ldapi
  [11/47]: configuring uniqueness plugin
  [12/47]: configuring uuid plugin
  [13/47]: configuring modrdn plugin
  [14/47]: configuring DNS plugin
  [15/47]: enabling entryUSN plugin
  [16/47]: configuring lockout plugin
  [17/47]: configuring topology plugin
  [18/47]: creating indices
  [19/47]: enabling referential integrity plugin
  [20/47]: configuring certmap.conf
  [21/47]: configure autobind for root
  [22/47]: configure new location for managed entries
  [23/47]: configure dirsrv ccache
  [24/47]: enabling SASL mapping fallback
  [25/47]: restarting directory server
  [26/47]: adding sasl mappings to the directory
  [27/47]: adding default layout
  [28/47]: adding delegation layout
  [29/47]: creating container for managed entries
  [30/47]: configuring user private groups
  [31/47]: configuring netgroups from hostgroups
  [32/47]: creating default Sudo bind user
  [33/47]: creating default Auto Member layout
  [34/47]: adding range check plugin
  [35/47]: creating default HBAC rule allow_all
  [36/47]: adding sasl mappings to the directory
  [37/47]: adding entries for topology management
  [38/47]: initializing group membership
  [39/47]: adding master entry
  [40/47]: initializing domain level
  [41/47]: configuring Posix uid/gid generation
  [42/47]: adding replication acis
  [43/47]: enabling compatibility plugin
  [44/47]: activating sidgen plugin
  [45/47]: activating extdom plugin
  [46/47]: tuning directory server
  [47/47]: configuring directory to start on boot
Done configuring directory server (dirsrv).
Configuring certificate server (pki-tomcatd). Estimated time: 3 minutes 30 seconds
  [1/31]: creating certificate server user
  [2/31]: configuring certificate server instance
  [3/31]: stopping certificate server instance to update CS.cfg
  [4/31]: backing up CS.cfg
  [5/31]: disabling nonces
  [6/31]: set up CRL publishing
  [7/31]: enable PKIX certificate path discovery and validation
  [8/31]: starting certificate server instance
  [9/31]: creating RA agent certificate database
  [10/31]: importing CA chain to RA certificate database
  [11/31]: fixing RA database permissions
  [12/31]: setting up signing cert profile
  [13/31]: setting audit signing renewal to 2 years
  [14/31]: restarting certificate server
  [15/31]: requesting RA certificate from CA
  [16/31]: issuing RA agent certificate
  [17/31]: adding RA agent as a trusted user
  [18/31]: authorizing RA to modify profiles
  [19/31]: authorizing RA to manage lightweight CAs
  [20/31]: Ensure lightweight CAs container exists
  [21/31]: configure certmonger for renewals
  [22/31]: configure certificate renewals
  [23/31]: configure RA certificate renewal
  [24/31]: configure Server-Cert certificate renewal
  [25/31]: Configure HTTP to proxy connections
  [26/31]: restarting certificate server
  [27/31]: migrating certificate profiles to LDAP
  [28/31]: importing IPA certificate profiles
  [29/31]: adding default CA ACL
  [30/31]: adding 'ipa' CA entry
  [31/31]: updating IPA configuration
Done configuring certificate server (pki-tomcatd).
Configuring directory server (dirsrv). Estimated time: 10 seconds
  [1/3]: configuring ssl for ds instance
  [2/3]: restarting directory server
  [3/3]: adding CA certificate entry
Done configuring directory server (dirsrv).
Configuring Kerberos KDC (krb5kdc). Estimated time: 30 seconds
  [1/9]: adding kerberos container to the directory
  [2/9]: configuring KDC
  [3/9]: initialize kerberos container
  [4/9]: adding default ACIs
  [5/9]: creating a keytab for the directory
  [6/9]: creating a keytab for the machine
  [7/9]: adding the password extension to the directory
  [8/9]: starting the KDC
  [9/9]: configuring KDC to start on boot
Done configuring Kerberos KDC (krb5kdc).
Configuring kadmin
  [1/2]: starting kadmin
  [2/2]: configuring kadmin to start on boot
Done configuring kadmin.
Configuring ipa_memcached
  [1/2]: starting ipa_memcached
  [2/2]: configuring ipa_memcached to start on boot
Done configuring ipa_memcached.
Configuring ipa-otpd
  [1/2]: starting ipa-otpd
  [2/2]: configuring ipa-otpd to start on boot
Done configuring ipa-otpd.
Configuring ipa-custodia
  [1/5]: Generating ipa-custodia config file
  [2/5]: Making sure custodia container exists
  [3/5]: Generating ipa-custodia keys
  [4/5]: starting ipa-custodia
  [5/5]: configuring ipa-custodia to start on boot
Done configuring ipa-custodia.
Configuring the web interface (httpd). Estimated time: 1 minute
  [1/21]: setting mod_nss port to 443
  [2/21]: setting mod_nss cipher suite
  [3/21]: setting mod_nss protocol list to TLSv1.0 - TLSv1.2
  [4/21]: setting mod_nss password file
  [5/21]: enabling mod_nss renegotiate
  [6/21]: adding URL rewriting rules
  [7/21]: configuring httpd
  [8/21]: configure certmonger for renewals
  [9/21]: setting up httpd keytab
  [10/21]: setting up ssl
  [11/21]: importing CA certificates from LDAP
  [12/21]: setting up browser autoconfig
  [13/21]: publish CA cert
  [14/21]: clean up any existing httpd ccache
  [15/21]: configuring SELinux for httpd
  [16/21]: create KDC proxy user
  [17/21]: create KDC proxy config
  [18/21]: enable KDC proxy
  [19/21]: restarting httpd
  [20/21]: configuring httpd to start on boot
  [21/21]: enabling oddjobd
Done configuring the web interface (httpd).
Applying LDAP updates
Upgrading IPA:
  [1/9]: stopping directory server
  [2/9]: saving configuration
  [3/9]: disabling listeners
  [4/9]: enabling DS global lock
  [5/9]: starting directory server
  [6/9]: upgrading server
  [7/9]: stopping directory server
  [8/9]: restoring configuration
  [9/9]: starting directory server
Done.
Restarting the directory server
Restarting the KDC
Configuring DNS (named)
  [1/11]: generating rndc key file
  [2/11]: adding DNS container
  [3/11]: setting up our zone
  [4/11]: setting up our own record
  [5/11]: setting up records for other masters
  [6/11]: adding NS record to the zones
  [7/11]: setting up kerberos principal
  [8/11]: setting up named.conf
  [9/11]: setting up server configuration
  [10/11]: configuring named to start on boot
  [11/11]: changing resolv.conf to point to ourselves
Done configuring DNS (named).
Configuring DNS key synchronization service (ipa-dnskeysyncd)
  [1/7]: checking status
  [2/7]: setting up bind-dyndb-ldap working directory
  [3/7]: setting up kerberos principal
  [4/7]: setting up SoftHSM
  [5/7]: adding DNSSEC containers
  [6/7]: creating replica keys
  [7/7]: configuring ipa-dnskeysyncd to start on boot
Done configuring DNS key synchronization service (ipa-dnskeysyncd).
Restarting ipa-dnskeysyncd
Restarting named
Updating DNS system records
Restarting the web server
Configuring client side components
Using existing certificate '/etc/ipa/ca.crt'.
Client hostname: cybertron.testrelm.test
Realm: TESTRELM.TEST
DNS Domain: testrelm.test
IPA Server: cybertron.testrelm.test
BaseDN: dc=testrelm,dc=test

Skipping synchronizing time with NTP server.
New SSSD config will be created
Configured sudoers in /etc/nsswitch.conf
Configured /etc/sssd/sssd.conf
trying https://cybertron.testrelm.test/ipa/json
Forwarding 'schema' to json server 'https://cybertron.testrelm.test/ipa/json'
trying https://cybertron.testrelm.test/ipa/session/json
Forwarding 'ping' to json server 'https://cybertron.testrelm.test/ipa/session/json'
Forwarding 'ca_is_enabled' to json server 'https://cybertron.testrelm.test/ipa/session/json'
Systemwide CA database updated.
Adding SSH public key from /etc/ssh/ssh_host_rsa_key.pub
Adding SSH public key from /etc/ssh/ssh_host_ecdsa_key.pub
Adding SSH public key from /etc/ssh/ssh_host_ed25519_key.pub
Forwarding 'host_mod' to json server 'https://cybertron.testrelm.test/ipa/session/json'
SSSD enabled
Configured /etc/openldap/ldap.conf
Configured /etc/ssh/ssh_config
Configured /etc/ssh/sshd_config
Configuring testrelm.test as NIS domain.
Client configuration complete.

==============================================================================
Setup complete

Next steps:
	1. You must make sure these network ports are open:
		TCP Ports:
		  * 80, 443: HTTP/HTTPS
		  * 389, 636: LDAP/LDAPS
		  * 88, 464: kerberos
		  * 53: bind
		UDP Ports:
		  * 88, 464: kerberos
		  * 53: bind
		  * 123: ntp
2. You can now obtain a kerberos ticket using the command: 'kinit admin'
	   This ticket will allow you to use the IPA tools (e.g., ipa user-add)
	   and the web user interface.

Be sure to back up the CA certificates stored in /root/cacert.p12
These files are required to create replicas. The password for these
files is the Directory Manager password</pre>

Create a user
--------------

Now, we will create a FreeIPA User which will be used in client authentication.

<pre>
[root@cybertron ~]# echo Secret123 | kinit admin
Password for admin@TESTRELM.TEST:
[root@cybertron temp]# echo Secret123 | ipa user-add --first testuser1 --last testuser1 testuser1 --password
----------------------
Added user "testuser1"
----------------------
  User login: testuser1
  First name: testuser1
  Last name: testuser1
  Full name: testuser1 testuser1
  Display name: testuser1 testuser1
  Initials: tt
  Home directory: /home/testuser1
  GECOS: testuser1 testuser1
  Login shell: /bin/sh
  Principal name: testuser1@TESTRELM.TEST
  Principal alias: testuser1@TESTRELM.TEST
  Email address: testuser1@testrelm.test
  UID: 539800003
  GID: 539800003
  Password: True
  Member of groups: ipausers
  Kerberos keys available: True</pre>

Issue user certificate using FreeIPA
------------------------------------

FreeIPA provides user certificates which can be used in client certificate authentication

<pre>
[root@cybertron ~]# ipa cert-request testuser1.csr --principal=testuser1@TESTRELM.TEST
  Issuing CA: ipa
  Certificate: MIIEDzCCAvegAwIBAgIBCzANBgkqhkiG9w0BAQsFADA4MRYwFAYDVQQKDA1URVNUUkVMTS5URVNUMR4wHAYDVQQDDBVDZXJ0aWZpY2F0ZSBBdXRob3JpdHkwHhcNMTcwMTE2MTExMjQyWhcNMTkwMTE3MTExMjQyWjAsMRYwFAYDVQQKDA1URVNUUkVMTS5URVNUMRIwEAYDVQQDDAl0ZXN0dXNlcjEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDM4943Ob29NVHgGZp+3WBAJ6mvOTTMjMfpmGy403jV1OUjDAfpTiMzye9TRCG83nUmGIH4CGI7rnbXtII3amEZKHjD6IRZWy/JLd6mvVL/Ab5P2GyInLvO5RFFFyzKcKQZix5GOHAGUXnX/uasB0lSQXazP+2tCKfsLdLCAnBCxZvatHcfFOK144STi4eNxnuTZHAgVU/zLclKVB6TK/8JfeX+/yyaeJUuAy/Zb5VmVu23NsIAQQxuGgzRZXQ2zoUuNi8MIwBm6bJoxVNiYhIyrXSTPzy/7lG4RHX8rseHkH8x1Xy+FHfkxAF49CTgYGKcMDh5gbEe6WCXdICAx+hHAgMBAAGjggEuMIIBKjAfBgNVHSMEGDAWgBQY/O/BU12jCr6vNtv674I0pv2IOTA/BggrBgEFBQcBAQQzMDEwLwYIKwYBBQUHMAGGI2h0dHA6Ly9pcGEtY2EudGVzdHJlbG0udGVzdC9jYS9vY3NwMA4GA1UdDwEB/wQEAwIE8DAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIweAYDVR0fBHEwbzBtoDWgM4YxaHR0cDovL2lwYS1jYS50ZXN0cmVsbS50ZXN0L2lwYS9jcmwvTWFzdGVyQ1JMLmJpbqI0pDIwMDEOMAwGA1UECgwFaXBhY2ExHjAcBgNVBAMMFUNlcnRpZmljYXRlIEF1dGhvcml0eTAdBgNVHQ4EFgQUI3v2p7d+WDzcjyghbIFqDyhnTXYwDQYJKoZIhvcNAQELBQADggEBAMaq+VnGPOi5d9LhY2OomI9tThNebpJf118U/WPAKSdGP/ptYFARtjkdHYPmb7XNVYqI6qloTUHVCU5WxMsCmt6ElayCeTbazr5l7mfkTpY2XvAxtI8UWcNMQiOF/YaZBjYCQOPFwfjlAdJ49RjRcXnFxsZ9lq2xFhyeYOLUx7GqFM5O+Sw7UpLPYpZ29i4fUmEdsbnFq57ep9bxrNhUjxruchOHI9BhWcxAwuguurxOoOvpVurmgC96vlpl0thBtcbkUV6eAbnY6nX2VQ4p9vpqL90cCVz4EEaMTW1Aw4VzZqS3UzkMLP4yCLfs5eI/P4/wdG3XhD9axkPgcdy60Ns=
  Subject: CN=testuser1,O=TESTRELM.TEST
  Issuer: CN=Certificate Authority,O=TESTRELM.TEST
  Not Before: Mon Jan 16 11:12:42 2017 UTC
  Not After: Thu Jan 17 11:12:42 2019 UTC
  Fingerprint (MD5): 12:cd:91:d9:a3:46:74:b2:47:ec:b7:68:e0:5a:bc:59
  Fingerprint (SHA1): 32:3e:b6:c2:c8:91:81:d2:15:65:51:d0:2d:de:a9:95:38:e5:04:ea
  Serial number: 11
  Serial number (hex): 0xB</pre>  

Issue Server certificate for httpd server
-----------------------------------------

<pre>[root@cybertron temp]# ipa cert-request server1.csr --principal=http/tiger.testrelm.test@TESTRELM.TEST --add
  Issuing CA: ipa
  Certificate: MIIEGjCCAwKgAwIBAgIBDDANBgkqhkiG9w0BAQsFADA4MRYwFAYDVQQKDA1URVNUUkVMTS5URVNUMR4wHAYDVQQDDBVDZXJ0aWZpY2F0ZSBBdXRob3JpdHkwHhcNMTcwMTE2MTE0MTA2WhcNMTkwMTE3MTE0MTA2WjA3MRYwFAYDVQQKDA1URVNUUkVMTS5URVNUMR0wGwYDVQQDDBR0aWdnZXIudGVzdHJlbG0udGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKI0ZHoJL4h4g8WYovnSc7JA1v/Fs7spG9fEphzKC0dsOGPeFz9O39GH/xZDnVizg9wcD7dqHevHPSjIDa/4Myi7y86AUqWgLZPBLX9PXcStunFi/KbJngJza6DqqB6s6g6f0Nsex4ff+CuaJll6M8WaIdO0piavlZdiff3ciOvTvq0HiE4LPEHdt812Owk6xojF/5lOgoQKtsd7kzZ79DWxSTQQ7XLgvh4dr4cKNhBIpMLjAENSLfqIQ9QyGdOSZICY95fmgQJGIwmnzun7wfoabedYvB3ZsvsexRT+bZ3PIxDaPoT8gFW69d2qu65/Sp32dsq97rNQ0TBW/CmKdR8CAwEAAaOCAS4wggEqMB8GA1UdIwQYMBaAFBj878FTXaMKvq822/rvgjSm/Yg5MD8GCCsGAQUFBwEBBDMwMTAvBggrBgEFBQcwAYYjaHR0cDovL2lwYS1jYS50ZXN0cmVsbS50ZXN0L2NhL29jc3AwDgYDVR0PAQH/BAQDAgTwMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjB4BgNVHR8EcTBvMG2gNaAzhjFodHRwOi8vaXBhLWNhLnRlc3RyZWxtLnRlc3QvaXBhL2NybC9NYXN0ZXJDUkwuYmluojSkMjAwMQ4wDAYDVQQKDAVpcGFjYTEeMBwGA1UEAwwVQ2VydGlmaWNhdGUgQXV0aG9yaXR5MB0GA1UdDgQWBBQ7DX/T/1VjuTNnFP6bcsVJgmFkhzANBgkqhkiG9w0BAQsFAAOCAQEAqpPf4eDPkYzmUa1PxmwGr96du0pX9OZyZn1uVqDLlusRvtTR0u0GY6dtk55BNrsbCbIPDMN11XaX3pajfCxNqWsNJaaPMV0s3JjgmLukZqCTF5NsmBkuz6OYnwqvTm5n6GLlMQWUisbwUdm0j6fSA4t9qvQHIafT5mS6dUZhS1LpGG6j/R3ycVdMaVDVIbu0zc9tzNxo8ebb6+f0UyHZ7UpavKMeJGo5vWwwHm52BBKR4WzN3VFMoyrxbCG7ctLw1MjOsLqEl+dz7IilWHidrEDnWAc0duC+AJ/hUo13zk3tqITOnSb99yoNhGhtO9PU/OqoMlr8LW/FhNrOv2W4/Q==
  Subject: CN=tiger.testrelm.test,O=TESTRELM.TEST
  Issuer: CN=Certificate Authority,O=TESTRELM.TEST
  Not Before: Mon Jan 16 11:41:06 2017 UTC
  Not After: Thu Jan 17 11:41:06 2019 UTC
  Fingerprint (MD5): b6:70:4b:f9:c0:0b:78:d9:52:a1:41:3d:6d:f7:55:01
  Fingerprint (SHA1): 84:43:b5:ee:f6:cc:0d:dc:9e:f0:e7:1a:91:c4:eb:b4:42:c5:10:ae
  Serial number: 12
  Serial number (hex): 0xC</pre>


Installing mod_nss on httpd server
----------------------------------

Let us install mod_nss on httpd server i.e. `tiger.testrelm.test`

<pre>[root@tiger ~]# yum install -y mod_nss
Failed to set locale, defaulting to C
Loaded plugins: product-id, search-disabled-repos, security, subscription-manager
This system is not registered with an entitlement server. You can use subscription-manager to register.
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package mod_nss.x86_64 0:1.0.10-9.el6 will be installed
beaker-Server/filelists_db                                                                               | 3.4 MB     00:00
--> Processing Dependency: httpd-mmn = 20051115 for package: mod_nss-1.0.10-9.el6.x86_64
--> Processing Dependency: httpd for package: mod_nss-1.0.10-9.el6.x86_64
--> Running transaction check
---> Package httpd.x86_64 0:2.2.15-59.el6 will be installed
--> Processing Dependency: httpd-tools = 2.2.15-59.el6 for package: httpd-2.2.15-59.el6.x86_64
--> Processing Dependency: apr-util-ldap for package: httpd-2.2.15-59.el6.x86_64
--> Running transaction check
---> Package apr-util-ldap.x86_64 0:1.3.9-3.el6_0.1 will be installed
---> Package httpd-tools.x86_64 0:2.2.15-59.el6 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================================================================
 Package                        Arch                    Version                            Repository                      Size
================================================================================================================================
Installing:
 mod_nss                        x86_64                  1.0.10-9.el6                       beaker-Server                   96 k
Installing for dependencies:
 apr-util-ldap                  x86_64                  1.3.9-3.el6_0.1                    beaker-Server                   15 k
 httpd                          x86_64                  2.2.15-59.el6                      beaker-Server                  833 k
 httpd-tools                    x86_64                  2.2.15-59.el6                      beaker-Server                   79 k

Transaction Summary
================================================================================================================================
Install       4 Package(s)

Total download size: 1.0 M
Installed size: 3.4 M
Downloading Packages:
(1/4): apr-util-ldap-1.3.9-3.el6_0.1.x86_64.rpm                                                          |  15 kB     00:00
(2/4): httpd-2.2.15-59.el6.x86_64.rpm                                                                    | 833 kB     00:00
(3/4): httpd-tools-2.2.15-59.el6.x86_64.rpm                                                              |  79 kB     00:00
(4/4): mod_nss-1.0.10-9.el6.x86_64.rpm                                                                   |  96 kB     00:00
--------------------------------------------------------------------------------------------------------------------------------
Total                                                                                            23 MB/s | 1.0 MB     00:00
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing : apr-util-ldap-1.3.9-3.el6_0.1.x86_64                                                                         1/4
  Installing : httpd-tools-2.2.15-59.el6.x86_64                                                                             2/4
  Installing : httpd-2.2.15-59.el6.x86_64                                                                                   3/4
  Installing : mod_nss-1.0.10-9.el6.x86_64                                                                                  4/4
  Verifying  : mod_nss-1.0.10-9.el6.x86_64                                                                                  1/4
  Verifying  : httpd-tools-2.2.15-59.el6.x86_64                                                                             2/4
  Verifying  : httpd-2.2.15-59.el6.x86_64                                                                                   3/4
  Verifying  : apr-util-ldap-1.3.9-3.el6_0.1.x86_64                                                                         4/4

Installed:
  mod_nss.x86_64 0:1.0.10-9.el6

Dependency Installed:
  apr-util-ldap.x86_64 0:1.3.9-3.el6_0.1         httpd.x86_64 0:2.2.15-59.el6         httpd-tools.x86_64 0:2.2.15-59.el6

Complete!</pre>


Remove pre-installed certificates from httpd's NSSdb
----------------------------------------------------

We need to remove pre-installed certificates (provided by httpd installation)

<pre>[root@tiger ~]# certutil -D -d /etc/httpd/alias/ -n cacert
[root@tiger ~]# for i in beta alpha Server-Cert cacert
> do
> certutil -D -d /etc/httpd/alias/ -n $i
> done
[root@tiger ~]# certutil -L -d /etc/httpd/alias/

Certificate Nickname                                         Trust Attributes
                                                             SSL,S/MIME,JAR/XPI

</pre>


Import CA certificate and Server certificate on httpd server
--------------------------------------------------------------

Import previously created CA certificate and server certificate in httpd's NSSdb

First export CA certificate and server certificate from `cybertron`

<pre>[root@cybertron ~]# ipa cert-show 12 --out=server1.crt
[root@cybertron ~]# ipa cert-show 11 --out=testuser1.crt
[root@cybertron ~]# openssl pkcs12 -in cacert.p12 -clcerts -nokeys -out cacert.crt
Enter Import Password:
MAC verified OK</pre>

Now, import these certificates on httpd server i.e., `tiger`

<pre>[root@tiger alias]# pwd
/etc/httpd/alias
[root@tiger alias]# pk12util -i server1.p12 -d .
Enter password for PKCS12 file:
pk12util: no nickname for cert in PKCS12 file.
pk12util: using nickname: tiger.testrelm.test - TESTRELM.TEST
pk12util: PKCS12 IMPORT SUCCESSFUL
[root@tiger alias]# pk12util -i cacert.p12 -d .
Enter password for PKCS12 file:
pk12util: PKCS12 IMPORT SUCCESSFUL
[root@tiger alias]# certutil -L -d .

Certificate Nickname                                         Trust Attributes
                                                             SSL,S/MIME,JAR/XPI

tiger.testrelm.test - TESTRELM.TEST                         u,u,u
ocspSigningCert cert-pki-ca                                  u,u,u
subsystemCert cert-pki-ca                                    u,u,u
Certificate Authority - TESTRELM.TEST                        u,u,u
auditSigningCert cert-pki-ca                                 u,u,u
[root@tiger alias]# certutil -M -d . -t 'CTu,Cu,Cu' -n 'Certificate Authority - TESTRELM.TEST'
[root@tiger alias]# certutil -L -d .

Certificate Nickname                                         Trust Attributes
                                                             SSL,S/MIME,JAR/XPI

tiger.testrelm.test - TESTRELM.TEST                         u,u,u
ocspSigningCert cert-pki-ca                                  u,u,u
subsystemCert cert-pki-ca                                    u,u,u
auditSigningCert cert-pki-ca                                 u,u,u
Certificate Authority - TESTRELM.TEST                        CTu,Cu,Cu</pre>


Create a virtualhost for authentication purpose
------------------------------------------------

First, create a secure directory for which we want to have authentication

<pre>[root@tiger ~]# mkdir /var/www/secure
[root@tiger ~]# echo "Hello" > /var/www/secure/index.html</pre>

Now, create a virtualhost configuration for secure directory by create a file - `/etc/httpd/conf.d/secure.conf`

Contents of `secure.conf`

<pre>NameVirtualHost 192.168.12.2:8443
LoadModule nss_module modules/libmodnss.so
Listen 8443
< VirtualHost _default_:8443>
    ServerName tiger.testrelm.test
    DocumentRoot /var/www/secure

    NSSEngine on
    NSSCertificateDatabase /etc/httpd/alias
    NSSOCSP on
    NSSOCSPTimeout 10
    NSSOCSPMinCacheEntryDuration 60
    NSSOCSPMaxCacheEntryDuration 80
    NSSRenegotiation on
    NSSPassPhraseDialog  builtin
    NSSPassPhraseHelper /usr/libexec/nss_pcache

    NSSCipherSuite +rsa_3des_sha,+rsa_aes_128_sha,+rsa_aes_256_sha,+ecdh_ecdsa_3des_sha,+ecdh_ecdsa_aes_256_sha,+ecdhe_ecdsa_3des_sha,+ecdhe_ecdsa_aes_256_sha,+ecdh_rsa_3des_sha,+ecdh_rsa_aes_256_sha,+ecdhe_rsa_3des_sha,+ecdhe_rsa_aes_128_sha,+ecdhe_rsa_aes_256_sha

    NSSProtocol TLSv1.0,TLSv1.1

    NSSNickname "tiger.testrelm.test - TESTRELM.TEST"

    NSSVerifyClient require
    LogLevel debug
    NSSRequireSafeNegotiation On
    NSSEnforceValidCerts On
< /VirtualHost>
</pre>

P.S. remove space from Virtualhost Tags

Restart httpd Server
----------------------

<pre>[root@tiger ~]# /etc/init.d/httpd restart
Stopping httpd: [  OK  ]
Starting httpd: [  OK  ]</pre>

Test configuration using curl
------------------------------

Let us test configuration using `curl` command

<pre>[root@client ~]# curl -vvl https://`hostname`:8443 --cacert /temp/cacert.crt --cert /temp/testuser1.crt --key /temp/testuser1.key
* About to connect() to tiger.testrelm.test port 8443 (#0)
*   Trying 192.168.12.2... connected
* Connected to tiger.testrelm.test (192.168.12.2) port 8443 (#0)
* Initializing NSS with certpath: sql:/etc/pki/nssdb
*   CAfile: /root/temp/cacert.crt
  CApath: none
* NSS: client certificate from file
* 	subject: CN=testuser1,O=TESTRELM.TEST
* 	start date: Jan 16 11:12:42 2017 GMT
* 	expire date: Jan 17 11:12:42 2019 GMT
* 	common name: testuser1
* 	issuer: CN=Certificate Authority,O=TESTRELM.TEST
* SSL connection using TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
* Server certificate:
* 	subject: CN=tiger.testrelm.test,O=TESTRELM.TEST
* 	start date: Jan 16 11:41:06 2017 GMT
* 	expire date: Jan 17 11:41:06 2019 GMT
* 	common name: tiger.testrelm.test
* 	issuer: CN=Certificate Authority,O=TESTRELM.TEST
> GET / HTTP/1.1
> User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.19.1 Basic ECC zlib/1.2.3 libidn/1.18 libssh2/1.4.2
> Host: tiger.testrelm.test:8443
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Tue, 17 Jan 2017 08:51:55 GMT
< Server: Apache/2.2.15 (Red Hat)
< Last-Modified: Mon, 16 Jan 2017 12:01:46 GMT
< ETag: "e0351-6-54634f29ce826"
< Accept-Ranges: bytes
< Content-Length: 6
< Connection: close
< Content-Type: text/html; charset=UTF-8
<
Hello
* Closing connection #0</pre>

Check if OCSP from IPA server works or Not
------------------------------------------

Stop FreeIPA service on `cybertron`

<pre>[root@cybertron ~]# ipactl stop
Stopping ipa-dnskeysyncd Service
Stopping ipa-otpd Service
Stopping ntpd Service
Stopping ipa-custodia Service
Stopping httpd Service
Stopping ipa_memcached Service
Stopping named Service
Stopping kadmin Service
Stopping krb5kdc Service
Stopping Directory Service
ipa: INFO: The ipactl command was successful</pre>


Now, check client certification authentication using curl command

<pre>[root@client ~]# curl -vvl https://`hostname`:8443 --cacert /temp/cacert.crt --cert /temp/testuser1.crt --key /temp/testuser1.key
* About to connect() to tiger.testrelm.test port 8443 (#0)
*   Trying 192.168.12.2... connected
* Connected to tiger.testrelm.test (192.168.12.2) port 8443 (#0)
* Initializing NSS with certpath: sql:/etc/pki/nssdb
*   CAfile: /root/temp/cacert.crt
  CApath: none
* NSS: client certificate from file
* 	subject: CN=testuser1,O=TESTRELM.TEST
* 	start date: Jan 16 11:12:42 2017 GMT
* 	expire date: Jan 17 11:12:42 2019 GMT
* 	common name: testuser1
* 	issuer: CN=Certificate Authority,O=TESTRELM.TEST
* NSS error -12271
* Closing connection #0
* SSL connect error
curl: (35) SSL connect error</pre>

Check httpd logs on `tiger`

<pre>[root@tiger httpd]# tail -f /var/log/httpd/error_log
[Tue Jan 17 04:09:01 2017] [debug] nss_engine_init.c(1948): SNI: Found nickname tiger.testrelm.test - TESTRELM.TEST for vhost: tiger.testrelm.test
[Tue Jan 17 04:09:01 2017] [debug] nss_engine_init.c(1970): SNI: Successfully paired vhost tiger.testrelm.test with nickname: tiger.testrelm.test - TESTRELM.TEST
[Tue Jan 17 04:09:01 2017] [error] Bad remote server certificate: -8071
[Tue Jan 17 04:09:01 2017] [error] SSL Library Error: -8071 The OCSP server experienced an internal error
[Tue Jan 17 04:09:01 2017] [info] SSL input filter read failed.
[Tue Jan 17 04:09:01 2017] [error] SSL Library Error: -8071 The OCSP server experienced an internal error
[Tue Jan 17 04:09:01 2017] [info] Connection to child 3 closed (server tiger.testrelm.test:443, client 192.168.12.2)</pre>
