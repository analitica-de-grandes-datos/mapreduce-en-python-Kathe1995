#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == "__main__":

    curkey = None
    total = 0
    for line in sys.stdin:

        key, value = line.split(",")
        value = int(value)

        if key == curkey:
            total += value
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))
            curkey= key
            total = value

    sys.stdout.write("{}\t{}\n".format(curkey, total))