with open("input6") as f:
    lines = f.readlines()


class Node:
    def __init__(self, name, parent, root):
        self.children = []
        self.name = name
        self.parent = parent
        self.root = root
        self.santa = False


net = []
for x in lines:
    if 'COM)' in x:
        root = Node('COM', None, True)
        net.append(root)
        break
i = 0
# Part 1
while True:
    cur = net[i]
    children = [x.strip()[4:] for x in lines if cur.name + ')' in x]
    for x in children:
        net.append(Node(x, cur, False))
        cur.children.append(len(net) - 1)
    i += 1
    if i >= len(lines):
        break
connects = 0
t = 0
for x in net:
    t += 1
    if not x.root:
        p = x
        while p.parent is not None:
            connects += 1
            p = p.parent
print(connects)

# Part 2
san = [x for x in net if 'SAN' in x.name][0]
san.santa = True
p = san
while p.parent is not None:
    p = p.parent
    p.santa = True
you = [x for x in net if 'YOU' in x.name][0]
cur = you.parent
distance = 0
while not cur.santa:
    distance += 1
    cur = cur.parent
while not 'SAN' in [net[x].name for x in cur.children]:
    distance += 1
    cur = [net[x] for x in cur.children if net[x].santa][0]
print(distance)
