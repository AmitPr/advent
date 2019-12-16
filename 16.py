with open("input16") as f:
    lines = f.readlines()
import math
def phase(x):
    out = []
    for i in range(len(x)):
        cur = 0
        s = 0
        for j in [int(v) for v in x]:
            pattern = math.ceil((cur-(i-1))/(i+1))%4
            s += j*[0,1,0,-1][pattern]
            cur+=1
        out.append(str(abs(s)%10))
    return ''.join(out)
def p2(x):
    su = sum(x)
    ans = []
    for i in range(len(x)):
        ans+=[((su %10)+ 10) %10]
        su-=x[i]
    return ans
cur = lines[0].strip()
cur = [int(x) for x in cur]
offset = int("".join(map(str,cur[:7])))
print(offset)
cur=cur*10000
cur = cur[int(offset):]
print('starting')
for i in range(100):
    cur = p2(cur)
#offset = int(cur[:8])
print(''.join(map(str,cur[:8])))
