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
