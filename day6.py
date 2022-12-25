input_file = open("input6.txt", 'r').read().strip()

# print(input_file)

visited = set()
# ans1 = 0
for i in range(len(input_file)-13):
  print(input_file[i:i+14])
  if len(set(input_file[i:i+14])) == 14:
    print(i+14)
    break


# print(ans1)