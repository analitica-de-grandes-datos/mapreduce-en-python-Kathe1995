#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
list = []

for row in sys.stdin:
  tupla = (row.strip().split(";")[0],row.strip().split(";")[1])
  list.append(tupla)
  list.sort(lambda x: x[1])
for tupla in list:
  letra = tupla[0]
  line =  letra + "," + str(tupla[1]) + "\n"
  sys.stdout.write(line) 