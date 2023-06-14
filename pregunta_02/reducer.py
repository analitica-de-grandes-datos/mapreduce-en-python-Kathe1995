import sys
if __name__ == '__main__':

    curkey = None
    value = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            if val > value:
                value = val
        else:
            if curkey is not None:
         
                sys.stdout.write("{}\t{}\n".format(curkey, value))

            curkey = key
            value = val

    sys.stdout.write("{}\t{}\n".format(curkey, value))
