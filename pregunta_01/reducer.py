#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

c = None
total = 0

for i in sys.stdin:
    
    key, value = i.split("\t") 
    value = int(value)
    
    if key == c: 
        total += value  
    else:
        if c is not None:
            sys.stdout.write("{}\t{}\n".format(c, total)) 
        
        c = key
        total = value

sys.stdout.write("{}\t{}\n".format(c, total)) 