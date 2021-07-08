#! /bin/bash

# cd /path/to/directory/containing/these/files # Uncomment to use this as a command (as well as cp cliDG.sh commandname; chmod +x commandname; mv commandname /usr/local/bin) 
rm test.* > /dev/null 2>&1 
py cliDG.py $@&& pdflatex diagram.tex&& open diagram.pdf
