Title: [Solved] Failed to connect, CredSSP required by server
Date: 2016-07-03 12:03
Modified: 2016-07-03 12:03
Category: Windows, rdesktop, Linux, Fedora 24
Tags: commandline, Windows, Linux, rdesktop
Slug: windows-rdesktop
Authors: Abhijeet Kasurde
Summary: [Solved] Failed to connect, CredSSP required by server

* While connecting to Windows Server using rdesktop from Linux server using 
following command like

    <pre>$ rdesktop -u Administrator -d akrelm.in 192.168.122.149 -p pa$$w0rd</pre>

    if you get this error

    <pre>Failed to connect, CredSSP required by server</pre>

    then,

    Run following registry edit command on Windows Server

    <pre>C:\\>reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f</pre>
