import sys

if __name__ == '__main__':

    curkey = None
    v_sum  = 0
    v_count  = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
     
            v_sum = v_sum + val  
            v_count =  v_count + 1

        else:
         
            if curkey is not None:
            
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_sum, v_sum/v_count))

            curkey = key
            v_sum = val
            v_count = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_sum, v_sum/v_count))
