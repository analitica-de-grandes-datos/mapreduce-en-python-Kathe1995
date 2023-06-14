#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for i in sys.stdin:
    sys.stdout.write(i.split(",")[2]+"\t1\n")