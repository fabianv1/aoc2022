input_file = [l.split(',') for l in open("input4.txt", 'r').readlines()]

count1 = 0
count2 = 0
for pair in input_file:
  first, second = pair
  s1, e1 = first.split('-')
  s2, e2 = second.split('-')
  if int(s1) <= int(s2) and int(e2) <= int(e1):
    count1 += 1
  elif int(s2) <= int(s1) and int(e1) <= int(e2):
    count1 += 1
  if len(set(range(int(s1), int(e1)+1)).intersection(set(range(int(s2), int(e2)+1)))):
    count2 += 1



print(count1)
print(count2)