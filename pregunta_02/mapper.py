#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    sys.stdout.write(line.split(",")[3]+"\t"+line.split(",")[4]+"\n")