#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
for row in sys.stdin:
  linea = row.strip().split(",")[0] + ";" + row.strip().split(",")[1]
  sys.stdout.write(linea+"\n")
