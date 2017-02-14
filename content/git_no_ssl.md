Title: Git commands without SSL verify
Date: 2017-02-14 12:03
Modified: 2017-02-14 12:03
Category: git
Tags: git, cheat-sheet
Slug: git-no-ssl-verify
Authors: Abhijeet Kasurde
Summary: Git commands without SSL verify

* Use git commands on a git server without proper SSL certificate 

    <pre>$ env GIT_SSL_NO_VERIFY=true git COMMAND</pre>

* To disable SSL certificate checking for repo only

    <pre>$ git config http.sslVerify "false"</pre>

* To disable SSL certificate checking for all repos

    <pre>$ git config --global http.sslVerify "false"</pre>
