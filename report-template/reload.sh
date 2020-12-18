#!/bin/bash
a="$(ls -clR | md5sum)";while $TRUE; do if [ "$a" == "$(ls -clR | md5sum)" ]; then sleep 0.1; else xelatex --interaction=nonstopmode report.tex >/dev/null;a="$(ls -clR | md5sum)"; fi; done
