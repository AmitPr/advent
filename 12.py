import numpy as np
moons = [(0, 4, 0, 0, 0, 0), (-10, -6, -14, 0, 0, 0),
         (9, -16, -3, 0, 0, 0), (6, -1, 2, 0, 0, 0)]
steps = 1000000
seenX, seenY, seenZ = set(), set(), set()
r = [0, 0, 0]
for i in range(steps):
    for j in range(len(moons)):
        for o in moons:
            if not moons[j] is o:
                pv = list(moons[j])
                pv[3], pv[4], pv[5] = pv[3] + np.sign(o[0] - pv[0]), pv[4] + np.sign(
                    o[1] - pv[1]), pv[5] + np.sign(o[2] - pv[2])
                moons[j] = tuple(pv)
    for j in range(len(moons)):
        x = list(moons[j])
        x[0], x[1], x[2] = x[0] + x[3], x[1] + x[4], x[2] + x[5]
        moons[j] = tuple(x)
    x = [[m[0], m[3]] for m in moons]
    if not r[0]:
        if str(x) in seenX:
            r[0] = i
        else:
            seenX.add(str(x))
    y = [[m[1], m[4]] for m in moons]

    if not r[1]:
        if str(y) in seenY:
            r[1] = i
        else:
            seenY.add(str(y))
    z = [[m[2], m[5]] for m in moons]

    if not r[2]:
        if str(z) in seenZ:
            r[2] = i
        else:
            seenZ.add(str(z))
    if not 0 in r:
        break
print(np.lcm.reduce(r))
d = []
i = 0
e = 0
for i in moons:
    pe = abs(i[0]) + abs(i[1]) + abs(i[2])
    ke = abs(i[3]) + abs(i[4]) + abs(i[5])
    e += pe * ke
print(e)
