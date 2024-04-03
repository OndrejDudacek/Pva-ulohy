import sys

numSequence = sys.argv[1].split()

if (len(numSequence) == 0 or len(numSequence) > 2000 or not all(map(lambda x: x.isdigit(), numSequence))):
    print("Nespravny vstup")
    sys.exit()

