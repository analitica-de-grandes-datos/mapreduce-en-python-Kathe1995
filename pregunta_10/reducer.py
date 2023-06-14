import sys 

if __name__ == '__main__': 
    curkey = None 
    total = 0 
 
    for line in sys.stdin: 
        key, val = line.split("\t") 
        val = val.strip() 
 
        if key == curkey: 
          
            n = n + ',' + str(int(val)) 
        else: 
         
            if curkey is not None: 
  
                sys.stdout.write("{}\t{}\n".format(curkey, n)) 
 
            curkey = key 
            n = str(int(val)) 
 
    sys.stdout.write("{}\t{}\n".format(curkey, n))
