import sys

if __name__ == '__main__':
    for line in sys.stdin:
        sys.stdout.write("{},{}\n".format(line.split(",")[1].strip(),line.split(",")[0]))
