import numpy as np
import pandas as pd
import operator

def diff_beads(beads):
    while beads:
        count = 0
        for b in zip(*map(lambda bead: bead[0] * bead[1], beads[:2])):
            yield from b
            count += 1
        beads = [(color, num - count) for color, num in beads[:2] if num - count > 0] + beads[2:]

def min_penalty(beads_in_grid):
    count = 0
    for i in range(0,len(beads_in_grid)):
        if beads_in_grid[-i] == beads_in_grid[-(i+1)]:
            a = beads_in_grid[-(i+1)]
            beads_in_grid[-(i+1)] = beads_in_grid[i]
            beads_in_grid[i] = a

def rotate(L, beads_in_grid):
    array = np.zeros((L, L), dtype=np.str)
    x, y = 0, 0
    res = 1
    array[x][y] = beads_in_grid[0]
    while (res < L*L):
        while (y+1 < L and not array[x][y+1]):
            res += 1
            y += 1
            array[x][y] = beads_in_grid[res-1]
        while (x+1 < L and (not array[x+1][y])):
            res += 1
            x += 1
            array[x][y] = beads_in_grid[res-1]
        while (y-1 >= 0 and not array[x][y-1]):
            res += 1
            y -= 1
            array[x][y] = beads_in_grid[res-1]
        while (x-1 >= 0 and not array[x-1][y]):
            res += 1
            x -= 1
            array[x][y] = beads_in_grid[res-1]
    return array

def countword(beats):
    x = np.zeros(5)
    for i in range(0,len(beats)):
        if beats[i] == 'R':
            x[0] += 1
        else if beats[i] == 'B':
            x[1] += 1
        else if beats[i] == 'G':
            x[2] += 1
        else if beats[i] == 'W':
            x[3] += 1
        else if beats[i] == 'Y':
            x[4] += 1
    print(x)

def coloring(L, beads):
    beads.sort(key=operator.itemgetter(1), reverse=True)
    beads_in_grid = list(diff_beads(beads))
    #print(beads_in_grid)
    min_penalty(beads_in_grid)
    #countword(beads_in_grid)
    result = rotate(L, beads_in_grid)
    return(result)

beads = [('R', 12), ('B', 13)]
a = coloring(5, beads)
df = pd.DataFrame(a)
df.to_csv('./output_question_5_1.txt', sep = ' ', index = 0, header = 0)

beads = [('R', 139), ('B', 1451), ('G', 977), ('W', 1072), ('Y', 457)]
a = coloring(64, beads)
df = pd.DataFrame(a)
df.to_csv('./output_question_5_2.txt', sep = ' ', index = 0, header = 0)