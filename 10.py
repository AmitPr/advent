import numpy as np
import math
import collections

with open("input10") as f:
    lines = f.readlines()
map = [[1 if x == '#' else 0 for x in line] for line in lines]
maxSeen = []
p = []
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x]:
            seen = []
            curPos = []
            for j in range(len(map)):
                for i in range(len(map[0])):
                    if i - x == 0 and y - j == 0:
                        continue
                    elif map[j][i]:
                        dX = i - x
                        dY = y - j
                        gcd = np.gcd(dX, dY)
                        if dX == 0:
                            slope = (0, np.sign(dY))
                        elif dY == 0:
                            slope = (np.sign(dX), 0)
                        else:
                            slope = (dX // gcd, dY // gcd)
                        if slope not in seen:
                            seen.append(slope)
            if len(seen) > len(maxSeen):
                maxSeen = seen
                p = (x, y)
print("Part 1:", len(maxSeen))
m = [math.atan2(x[1], x[0]) for x in maxSeen]
x = zip(m, maxSeen)
d = list(collections.OrderedDict(sorted(x, key=lambda x: (math.degrees(-1 * (2 * math.pi + x[0])) + 90 if x[0] < 0 else math.degrees(-1 * x[0]) + 90) if (math.degrees(-1 * (
    2 * math.pi + x[0])) + 90 if x[0] < 0 else math.degrees(-1 * x[0]) + 90) < 0 else (math.degrees(-1 * (2 * math.pi + x[0])) + 90 if x[0] < 0 else math.degrees(-1 * x[0]) + 90) - 360)).values())
k = d[199]
x, y = p[0], p[1]
x += k[0]
y -= k[1]
print("Part 2:", x * 100 + y)
