from collections import Counter

input_file = open("input3.txt", 'r').readlines()
prio = {}
for i in range(65, 91):
    prio[chr(i)] = i-(65-27)
for i in range(97, 123):
    prio[chr(i)] = i-(97-1)

_sum = 0
_sum2 = 0
seen2 = None
for i, line in enumerate(input_file):
    l = line.strip()
    n = int(len(l)/2)
    seen = set(l[:n])
    for c in l[n:]:
        if c in seen:
            _sum += prio[c]
            break
   
    # part 2
    if (i+1)%3==0:
        seen2 = seen2.intersection(set(l))
        _sum2 += prio[list(seen2)[0]]

    elif (i+1)%3 == 1:
        seen2 = set(l)
    else:
        seen2 = seen2.intersection(set(l))

print(_sum)
print(_sum2)
