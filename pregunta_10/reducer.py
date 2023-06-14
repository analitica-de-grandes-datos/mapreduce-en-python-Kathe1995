#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    d = None
    total = 0

    for i in sys.stdin:
        b, value = i.split("-")
        value = value.strip()

        if b == d:
            n = n + ',' + str(int(value))
        else:
            if d is not None:
                sys.stdout.write("{}\t{}\n".format(d, n))
            d= b
            n = str(int(value))

    sys.stdout.write("{}\t{}\n".format(d, n))