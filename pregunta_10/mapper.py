import sys
if __name__ == "__main__":
  
    for line in sys.stdin:
        key, val = line.split('\t') 
        val =list(val.strip().split(',')) 
        key = key.zfill(4) 
        
        for word in val: 
            sys.stdout.write("{}\t{}\n".format(word ,key))
