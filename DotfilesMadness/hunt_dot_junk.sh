#!/bin/bash

DOTF="$(ls -d ~/.??*)"

ALLOWED="bash_history bash_logout bash_profile bashrc cache config local ssh xinitrc pki"

for file in $DOTF
do
   [[ "$ALLOWED" != *"${file##*.}"* ]] && echo "$file"
done

