input_file = open("input1.txt", 'r').read().strip().split('\n')
set_ = set()
current_sum = 0
for line in input_file:
  # print(line)
  if line != '':
    current_sum += int(line)
  else:
    set_.add(current_sum)
    current_sum = 0
print(max(set_))
print(sum(sorted(set_, reverse=True)[:3]))
