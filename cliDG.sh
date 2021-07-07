#! /bin/bash

cd /Users/DaivdGlass/Downloads/Circuit-Diagram-Generator-main
rm test.* > /dev/null 2>&1 
py cliDG.py $@&& pdflatex test.tex&& open test.pdf
