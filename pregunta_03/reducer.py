#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
list = []

for row in sys.stdin:
  list.append((row.strip().split(";")[0],row.strip().split(";")[1]))
  list.sort(key=lambda k: k[1])
for t in list:
  sys.stdout.write(t[0] + "," + str(t[1]) + "\n") 