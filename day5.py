start_stack, procedures = map(lambda x: x.strip().split('\n'), open('input5.txt', 'r').read().split('\n\n'))

stacks = [[] for _ in range(9)]
for stack in start_stack[::-1]:
  i = 0
  for idx, c in enumerate(stack):
    if (idx - 1)%4 == 0:
      if c.isalpha():
        stacks[i].append(c)
      i += 1

for p in procedures:
  src, dest = int(p[-6]), int(p[-1])
  n = int(p.split()[1])
  to_append = []
  for _ in range(n):
    to_append.append(stacks[src-1].pop())
  # stacks[dest-1] += to_append
  stacks[dest-1] += to_append[::-1]

ans_1 = ''
for s in stacks:
  ans_1 += s[-1]

print(ans_1)