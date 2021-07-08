# Circuit-Diagram-Generator
This repository contains a stand alone python file (diagramGenerator.py) which generates a circuit diagram for a battery pack with s groups of p parallel cells, in series. 
This generates a .tex (LaTex) file which can then be compiled into a high quality pdf. In addition, there are two other files which automate the process further. 
cliDG.py takes the first two command line arguments as the number of groups and size of each group respectively. 
cliDG.sh also handles clean up of old files, compilation, and opening of the resulting PDF. 
