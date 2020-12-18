#!/bin/bash

if [[ "$PWD" == *hackthebox* &&  ! -d './'"$1" ]]
then
   mkdir './'"$1"
   cp -rL report-template lse.sh linpeas.sh pspy64 './'"$1"
   cp './prepReport.sh' './'"$1"'/report-template/'
   echo '\newcommand{\machinename}{'"$1"'}' >> './'"$1"/report-template/variables.tex
   echo -n "$(pwd)/$1"'/report-template/img' > ~/.config/screenshat/conf
fi

