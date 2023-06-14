import sys
if __name__ == "__main__":
    for line in sys.stdin:
        sys.stdout.write("{},1\n".format(line.split(" ")[0]))
