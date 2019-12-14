import collections
import math
with open("input14") as f:
    l = f.readlines()
reps = {}
for x in l:
    prod = x.split('=>')[1].strip()
    p_amt = int(prod.split(' ')[0])
    prod = str(prod.split(' ')[1])
    r = x.split('=>')[0].strip().split(',')
    reactants = []
    for x in r:
        x = x.strip()
        amt = int(x.split(' ')[0])
        name = str(x.split(' ')[1])
        reactants.append((name, amt))
    reps[prod] = (p_amt, reactants)


def fuel(amt):
    need = collections.defaultdict(int)
    need["FUEL"] = amt
    while True:
        keys = list(need.keys())
        cur = [x for x in list(need.keys()) if not 'ORE' in x and need[x] > 0]
        if len(cur) == 0:
            break
        cur = cur[0]
        amt, r = reps[cur]
        times = math.ceil(need[cur] / amt)
        need[cur] -= amt * times
        for n, amt in r:
            need[n] += amt * times
    return need["ORE"]


print(fuel(1))
lo = 0
hi = 10000000
target = 1000000000000
while lo < hi:
    avg = (lo + hi) // 2
    x = fuel(avg)
    if x < target:
        lo = avg + 1
    elif x > target:
        hi = avg - 1
    else:
        break
print('fuel', avg, 'ore', fuel(avg))
