with open("input8") as f:
    lines = f.readlines()
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
digits = [int(x) for x in lines[0].strip()]
x, y = 25, 6
layers = []
for i in range(0, len(digits), 25 * 6):
    cur = digits[i:i + 25 * 6]
    layers.append(cur)
zeros = [x.count(0) for x in layers]
least = 12941253215
leastInd = -1
for i in range(len(zeros)):
    if zeros[i] < least:
        least = zeros[i]
        leastInd = i
print(layers)
print(layers[leastInd].count(1) * layers[leastInd].count(2))
final = layers[0]
for i in range(len(final)):
    curL = 0
    while layers[curL][i] == 2:
        curL += 1
    final[i] = layers[curL][i]
plt.imsave('final.png', np.array(final).reshape(6, 25), cmap=cm.gray)
print(np.array(final).reshape(25, 6))
print(''.join([str(x) for x in final]))
