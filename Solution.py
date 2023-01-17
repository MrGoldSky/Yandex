import sys


def a():
    d = dict()
    if sys.argv[2] == "--sort":
        for i in range(2, len(sys.argv)):
            stri = sys.argv[i].split("=")
            d.append(tuple(stri[0], stri[1]))
            d = sorted(d, key=lambda x: x[1] in d)
    else:
        for i in range(1, len(sys.argv)):
            stri = sys.argv[i].split("=")
            print(f"key: {stri[0]} Value: {stri[1]}")


a()
