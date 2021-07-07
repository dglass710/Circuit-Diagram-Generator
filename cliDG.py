from diagramGenerator import main
import sys

for x in sys.argv[1:3]:
    try:
        int(x)
    except:
        sys.exit('s or p is not an int')
main(int(sys.argv[1]),int(sys.argv[2]),'test.tex')
