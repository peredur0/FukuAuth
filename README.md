# FukuAuth

Simple web application that manage authentication for a webapp

## Install
Create a post commit script to update the version.
File: `.git/hooks/post-merge`
```sh
#!/bin/sh
python3 scripts/update_version.py
git add .version
git commit -m "docs: version update after merge" --no-verify
```
Make it executable `chmod +x .git/hooks/post-merge`  

## Git workflow
```sh
# Create a new branch
git checkout -b feat/new-feature

# Work and commit on the new branch
# If the number of commit are greater than 1 (squash)
git rebase -i HEAD~X    # where X is the number of new commit

# Change all the commit from pick to squash except the last one
# ---
# pick a1b2c3 Commit 1
# squash d4e5f6 Commit 2
# squash 7890ab Commit 3
# save and close

# Write the commit message

# Do the merge
git checkout master
git merge feat/new-feature
git push --force origin master
```
