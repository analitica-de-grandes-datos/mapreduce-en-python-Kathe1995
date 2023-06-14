#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    c = None
    total = 0

    for line in sys.stdin:

        key, value = line.split("\t")
        value = int(value)

        if key == c:
            total += value
        else:
            if c is not None:
                sys.stdout.write("{},{}\n".format(c, total))

            c = key
            total = value

    sys.stdout.write("{},{}\n".format(c, total))