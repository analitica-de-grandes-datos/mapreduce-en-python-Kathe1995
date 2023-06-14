from operator import index
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        sys.stdout.write("{} {} {}\n".format( str(line.split('   ')[0]), line.split('   ')[2].strip().zfill(4) , line.split('   ')[1]))
