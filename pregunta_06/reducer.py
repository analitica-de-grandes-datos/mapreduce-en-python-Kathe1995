import sys
if __name__ == '__main__':
    curkey = None
    value_max  = 0
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
          
            if val > value_max:
                value_max = val
            if val < value_min:
                 value_min = val

        else:
     
            if curkey is not None:
          
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, value_max, value_min))

            curkey = key
            value_max = val
            value_min = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, value_max, value_min))
