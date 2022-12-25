input_file = list(map(lambda x: x.strip(), open("input9.txt", 'r').readlines()))

visited = set()
visited.add((0,0))
AMT = 10
snake = [(0,0) for _ in range(AMT)]

movement = {
  'U': (0, 1),
  'R': (1, 0),
  'D': (0, -1),
  'L': (-1, 0)
}

def is_adj(p, c):
  px, py = p
  cx, cy = c
  return abs(px-cx) <= 1 and abs(py-cy) <= 1

def update_pos(p, c):
  px, py = p
  cx, cy = c
  # same row or col
  if px == cx:
    return (cx, cy+1 if (py-cy)>0 else cy-1)
  if py == cy:
    return (cx+1 if (px-cx)>0 else cx-1, cy)
  
  # diff row and diff col
  return (cx+1 if (px-cx)>0 else cx-1, cy+1 if (py-cy)>0 else cy-1)

    
for i, line in enumerate(input_file):
  print(line)
  dir_, dist = line.split(' ')
  for _ in range(int(dist)):
    delta = movement[dir_]

    snake[0] = (snake[0][0] + delta[0], snake[0][1] + delta[1])
    for j  in range(1, AMT):
      prev_pos = snake[j-1]
      curr_pos = snake[j]
      if not is_adj(prev_pos, curr_pos):
        snake[j] = update_pos(prev_pos, curr_pos)
    visited.add(snake[AMT-1])
        
      
print(len(visited))
