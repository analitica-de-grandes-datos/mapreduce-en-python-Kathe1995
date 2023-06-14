#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    sys.stdout.write(line.split(" ")[0]+"\t1\n")