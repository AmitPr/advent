with open('input') as f:
    sum = 0
    for l in f.readlines():
        x = int(l.strip())
        x = (x // 3) - 2
        j = (x // 3) - 2
        while(j > 0):
            x += j
            j = (j // 3) - 2
        sum += x
    print(sum)
