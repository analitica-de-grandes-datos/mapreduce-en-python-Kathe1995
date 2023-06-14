#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
for row in sys.stdin:
  cantidad = row.strip().split(",")[1]
  letra = row.strip().split(",")[0]
  linea = letra + ";" + cantidad
  sys.stdout.write(linea+"\n")
