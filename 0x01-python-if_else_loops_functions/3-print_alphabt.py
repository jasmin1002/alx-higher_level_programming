#!/usr/bin/python3
asciiNumber = 97
while asciiNumber <= 122:
    if asciiNumber in [101, 113]:
        asciiNumber += 1
        continue

    print("{}".format(chr(asciiNumber)), end="")
    asciiNumber += 1
