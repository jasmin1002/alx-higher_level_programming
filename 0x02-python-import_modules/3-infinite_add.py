#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    accumulator = 0
    for i in range(1, len(sys.argv)):
        accumulator += int(sys.argv[i])
    print(accumulator)
