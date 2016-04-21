Title: Git - Cheatsheet
Date: 2016-03-11 12:03
Modified: 2016-03-11 12:03
Category: git
Tags: git
Slug: git-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Git - Cheatsheet

* Initialize bare repository

    <pre>$ git init .</pre>

* Amending the commit message which is not pushed

    <pre>$ git commit --amend</pre>

* Force push amended commit message to a remote branch

    <pre>$ git push remote_name branch_name -f</pre>

* Undo git add to files staged for git commit

    <pre>$ git reset HEAD file_name </pre> or
    <pre>$ git rm --cached file_name </pre>

    **Usage**: `git reset HEAD a.sh` or `git rm --cached a.sh`

    This command will remove a file named a.sh from the current index, the "about to be committed" area, without changing anything else.

* Diff files which are under staging

    <pre>$ git diff --staged </pre>

* Diff between two commits

    <pre>$ git diff commit_1 commit_2</pre>

* Diff between two branches

    <pre>$ git diff branch_1 branch_2</pre>

* Push Local branch to central git repository

    <pre>$ git push remote_name branch_name</pre>

* Create patch using git format-patch

    <pre>$ git format-patch master --stdout > fix_empty_poster.patch </pre>

* View first 3 commit messages in git log

    <pre>$ git log --pretty=oneline -3 </pre>

* Adding signed-off in commit message

    <pre>$ git commit -s -m "commit_message" </pre>

* Using pull without unwanted merge commits

    <pre>$ git pull --rebase </pre>

* Deleting last commit in local repository

    <pre>$ git reset HEAD^ --hard </pre>

* Deleting last commit from remote repository

    <pre>$ git reset HEAD^ --hard </pre>
    <pre>$ git push origin master -f </pre>

* Revert git pull

    <pre>$ git reset --hard </pre>

* Diff between lastest commit and last commit

    <pre>$ git diff HEAD^ HEAD</pre>
