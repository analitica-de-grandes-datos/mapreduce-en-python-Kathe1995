#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
dict =  {}

for row in sys.stdin:
  
  if row.strip().split(";")[0] in dict.keys():
    dict[row.strip().split(";")[0][0]] +=  1
    
  else:
    dict[row.strip().split(";")[0][0]] = 1


lista = [(i,dict[i]) for i in dict.keys()]
lista.sort(key=lambda x: x[0])

for t in lista:
  sys.stdout.write(str(t[0]) + "," + str(t[1]) + "\n") 