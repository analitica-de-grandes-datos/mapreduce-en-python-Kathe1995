

import sys

if __name__ == "__main__":
    contador = 0

    for line in sys.stdin:
        sys.stdout.write("{}   {}   {}\n".format(line.split('   ')[1], line.split('   ')[2].strip(), int(line.split('   ')[0]))) 
        if contador >= 5: 
            break 
        contador += 1
