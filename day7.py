input_file = open('input7.txt', 'r').readlines()

file_tree = {} # keys: directory path, values: list of dirs and files
dir_sizes = {}

current_dir = None
dir_stack = []
for i, line in enumerate(input_file):
  print('progress', i/len(input_file) * 100)
  if line[0] == '$': # command
    if 'cd' in line:  # change dir
      if '/' in line:
        current_dir = '/'
        dir_stack = ['/']
      elif '..' in line:
        current_dir = dir_stack.pop()
      else:
        current_dir = line.split(' ')[2].strip()
        dir_stack.append(current_dir)
    if 'ls' in line: # list
      pass
  else: # in list
    first, second = line.split(' ')
    key = tuple(dir_stack)
    if first == 'dir':
      sub = tuple(dir_stack + [second.strip()])
      file_tree[key] = file_tree.get(key, []) + [sub] # subdirectory
    else:
      file_tree[key] = file_tree.get(key, []) + [{int(first) : second.strip()}] # {size : filename}

for k, v in file_tree.items():
  print(f'{k}: {v}')

def get_size(k, running_sum):
  total = running_sum
  sub_elements = file_tree[k]
  for el in sub_elements:
    if isinstance(el, dict):
      total += list(el.keys())[0]
    else:
      total += get_size(el, 0)
  return total


for k, _ in file_tree.items():
  dir_sizes[
    k # directory  
  ] = get_size(k, running_sum=0) # size

threshold = 30000000 - (70000000 - dir_sizes[('/',)])
possible_to_free = []

ans1 = 0
# sum dirs <= 100000
for k, v in dir_sizes.items():
  if v <= 100000:
    ans1 += v
  if v >= threshold:
    possible_to_free.append((k, v))
# print(file_tree)

print(ans1)
print(min(possible_to_free, key=lambda x: x[1]))