#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 


for line in sys.stdin:
       sys.stdout.write("{},{},{}\n".format(int(line.split(",")[1]),line.split(',')[0],int(line.split(",")[1])))
