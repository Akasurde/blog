Title: Bash alias
Date: 2016-06-01 12:03
Modified: 2016-06-01 12:03
Category: bash
Tags: bash, alias, cheatsheet
Slug: alias-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Bash command alias


Following are some alias to make you work faster

* Alias for `cd` command

    <pre>
    alias cd..="cd .."
    alias 2..="cd ../.."
    alias 3..="cd ../../.."
    alias 4..="cd ../../../.."
    alias 5..="cd ../../../../.."
    </pre>

* Alias for `apt-get` command

    <pre>
    alias agi='apt-get install'
    alias agu='apt-get update'
    alias ags='apt-cache search'
    alias agsh='apt-cache show'
    alias agr='apt-get remove'
    alias agd='apt-get dist-upgrade'
    </pre>

* Alias for `ssh` command

    <pre>
    alias dev="user@dev.example.com -p 8000"
    alias prod="user@prod.example.com -p 8000"
    </pre>

* Alias for `df` command

    <pre>
    alias df="df -TPh"
    </pre>

* Alias for Port usages

    <pre>
    alias lsof="sudo lsof -i -P -sTCP:LISTEN"
    </pre>
