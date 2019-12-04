min = 246515
max = 739105
num_valids = 0
i = min
while i < max:
    digits = [int(x) for x in str(i)]
    if sorted(digits)!=digits:
        last = digits[0]
        problem=1
        for j in range(len(digits)):
            if digits[j] < last:
                problem = j
                break
            else:
                last = digits[j]
        digits[problem]+=1
        i=int(''.join(map(str,digits)))
    else:
        hasDouble=False
        for j in list(set(digits)):
            y= digits.count(j)
            if y==2:
                hasDouble=True
        if hasDouble:
            num_valids+=1
        i+=1
print(num_valids)
