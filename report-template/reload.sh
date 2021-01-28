#!/bin/bash
a="$(cat <(ls -clR) report.tex ./sections/*.tex | md5sum)"
while $TRUE
do if [ "$a" == "$(cat <(ls -clR) report.tex ./sections/*.tex | md5sum)" ]
then sleep 0.3
else xelatex --interaction=nonstopmode --shell-escape report.tex >/dev/null
   a="$(cat <(ls -clR) report.tex ./sections/*.tex | md5sum)"
   fi
done
