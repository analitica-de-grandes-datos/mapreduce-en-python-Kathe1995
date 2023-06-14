#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
l = []

for line in sys.stdin:
  l.append((line.strip().split(";")[0],line.strip().split(";")[1]))
  l.sort(key=lambda k: k[1])
for t in l:
  sys.stdout.write(t[0] + "," + str(t[1]) + "\n") 