#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
list = []

for row in sys.stdin:
  tupla=(row.strip().split(";")[0],row.strip().split(";")[1])
  list.append(tupla)
  list.sort(lambda k: k[1])
for tupla in list:
  sys.stdout.write(tupla[0] + "," + str(tupla[1]) + "\n") 