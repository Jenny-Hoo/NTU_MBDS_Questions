import os
import math

def readtxt(path):
    x = []
    y = []
    n = 0
    with open(path, encoding='utf-8') as files:
        for line in files:
            if line.strip() == "":
                continue
            line = line.replace('\n','').replace('\r','').split(" ")
            x.append(int(line[0]))
            y.append(int(line[1]))
            n += 1
    return x,y,n

def pnpoly(n, xp, yp, x, y):
    i = 0
    c = False
    j = n - 1
    while i < n:
        if (x == xp[i] and y == yp[i]) or (x == xp[j] and y == yp[j]):
            return 1
        if (yp[i] < y and yp[j] >= y) or (yp[i] >= y and yp[j] < y):
            _x = (xp[j] - xp[i]) * (y - yp[i]) / (yp[j] - yp[i]) + xp[i]
            if _x == x:
                return 1
            if x < _x:
                c = not c
        j = i
        i += 1
    return c

def main():
    xp, yp, np = readtxt('input_question_6_polygon.txt')
    x, y, n = readtxt('input_question_6_points.txt')
    out_path = "output_question_6.txt"
    files = open(out_path, 'w')
    for i in range(n):
        s = "inside" if pnpoly(np, xp, yp, x[i], y[i]) == 1 else "outside"
        # print("{} {} {}".format(x[i], y[i], s))
        files.write("{} {} {}".format(x[i], y[i], s))
        if i < n - 1:
            files.write("\n")


if __name__ == "__main__":
    main()
