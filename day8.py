input_file = [list(x.strip()) for x in open("input8.txt", 'r').readlines()]
R, C = len(input_file), len(input_file[0])
ans1 = 0
visible = set()

def traverse(range_, i, ir=False):
  last_visible = None
  ans = 0
  for j in range_:
    coord = (i, j) if ir else (j, i)
    tree = input_file[coord[0]][coord[1]]
    if last_visible == None:
      last_visible = int(tree)
      if coord not in visible:
        visible.add(coord)
        ans += 1
      continue
    
    if int(tree) > last_visible:
        last_visible = int(tree)
        if coord not in visible:
          visible.add(coord)
          ans += 1
  return ans

for r, line in enumerate(input_file):
  ans1 += traverse(range(C), r, True) # left to right
  ans1 += traverse(range(C-1, -1, -1), r, True) # right to left

for c in range(C):
  ans1 += traverse(range(R), c) # up to down
  ans1 += traverse(range(R-1, -1, -1), c) # down to up

ans2 = 0
for r in range(R):
  if r == 0 or r == R-1:
    continue
  for c in range(C):
    if c == 0 or c == C-1:
      continue
    tree = int(input_file[r][c])
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    score = 1
    for dr, dc in deltas:
      nr, nc = (r+dr, c+dc)

      next_ = int(input_file[nr][nc])
      sum_ = 1
      while next_ < tree:
        sum_ += 1
        nr, nc = (nr+dr, nc+dc)
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
          sum_ -= 1
          break
        next_ = int(input_file[nr][nc])
      score *= sum_
    ans2 = max(score, ans2)


print(ans1)
print(ans2)