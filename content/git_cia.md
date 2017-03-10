Title: Git - CIA cheatsheet
Date: 2017-11-03 12:03
Modified: 2016-11-03 12:03
Category: git
Tags: git
Slug: git-cheat-sheet-cia-edition
Authors: Abhijeet Kasurde
Summary: Git - CIA Cheatsheet

Shamelessly taken from - https://wikileaks.org/ciav7p1/cms/page_1179773.html
* List Aliases

    <pre>$ git config --get-regexp 'alias.*' | colrm 1 6 </pre>

* Use last commit message for amend

    <pre>$ git commit --amend -C HEAD </pre>

* Undo last commit and bring everything to staging area

    <pre>$ git reset --soft HEAD^ </pre>

* Undo last commit and restart everything

    <pre>$ git reset --hard HEAD^ </pre>

* Create new branch with Stash changes

    <pre>$ git stash branch new-branch-name </pre>

* Git status in short format

    <pre>$ git status -s </pre>
