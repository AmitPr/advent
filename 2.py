import sys
if sys.argv[1]==1:
    l = [int(x) for x in open("input2").read().split(',')]
    l[1]=12
    l[2]=2
    l = [int(x) for x in l]
    i=0
    while True:
        x = l[i]
        if x==1:
            one = l[i+1]
            two = l[i+2]
            three = l[i+3]
            l[three]=l[one]+l[two]
        elif x ==2:
            one = l[i+1]
            two = l[i+2]
            three = l[i+3]
            l[three]=l[one]*l[two]
        else:
            assert x == 99
            break
        i+=4
    print(','.join([str(x) for x in l]))
else:
    for k in range(0,100):
        for j in range(100):
            l = [int(x) for x in open("input2").read().split(',')]
            l[1]=k
            l[2]=j
            l = [int(x) for x in l]
            i=0
            while True:
                x = l[i]
                if x==1:
                    one = l[i+1]
                    two = l[i+2]
                    three = l[i+3]
                    l[three]=l[one]+l[two]
                elif x ==2:
                    one = l[i+1]
                    two = l[i+2]
                    three = l[i+3]
                    l[three]=l[one]*l[two]
                else:
                    assert x == 99
                    break
                i+=4
            if l[0]==19690720:
                print(100*k + j)
