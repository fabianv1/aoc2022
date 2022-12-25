input_file = open("input10.txt", 'r').readlines()

ans1 = 0
sum_ = 1
count = 1

for line in input_file:
  if count in [20, 60, 100, 140, 180, 220]:
    ans1 += count * sum_
  l = line.strip()
  if l == 'noop':
    count += 1
    continue
  _, val = l.split(' ')
  count += 1
  if count in [20, 60, 100, 140, 180, 220]:
    ans1 += count * sum_
  sum_ += int(val)
  count += 1


ans2 = [' ']*240
x = 1
cycle = 1

for line in input_file:
  l = line.strip()
  if (cycle%40)-1 in range(x-1, x+2):
    ans2[cycle-1] = '#'

  if l == 'noop':
    cycle += 1
    continue

  _, val = l.split(' ')
  cycle += 1
  if (cycle%40)-1 in range(x-1, x+2):
    ans2[cycle-1] = '#'

  x += int(val)
  cycle += 1

readable_ans2 = ''
for i in range(240):
  if (i+1)%40 == 0:
    readable_ans2 += ans2[i] + '\n'
  else:
    readable_ans2 += ans2[i]

print(ans1)
print(readable_ans2)