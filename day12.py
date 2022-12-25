import collections

height_map = [list(x.strip()) for x in open("input12.txt", 'r').readlines()]
start = None
end = None
lowest = []
R, C = len(height_map), len(height_map[0])
for r in range(R):
    for c in range(C):
        if height_map[r][c] == 'S':
            start = (r,c)
        if height_map[r][c] == 'E':
            end = (r,c)
        if height_map[r][c] == 'a':
            lowest.append((r,c))


def visualization(path):
    output = ''
    for r in range(R):
        for c in range(C):
            if (r, c) in path:
                output += height_map[r][c]
            else:
                output += ' '
        output += '\n'
    print(output)
            
# queue = collections.deque([[start]])
# visited = set(start)
visited = set()
queue = collections.deque([[x] for x in lowest])
steps = None
while queue:
    curr_path = queue.popleft()
    curr = curr_path[-1]
    curr_val = ord(height_map[curr[0]][curr[1]])
    
    
    # neighbors
    delta = [(0,1), (0,-1), (1,0), (-1,0)]
    new_paths = []
    for dr, dc in delta:
        new_r, new_c = dr+curr[0], dc+curr[1]
        if new_r in range(R) and new_c in range(C):
            new_val = ord(height_map[new_r][new_c])
            if (new_r, new_c) == end:
                if chr(curr_val) == 'z':
                    visualization(curr_path)
                    steps = len(curr_path)
                    queue = []
                    break

            if (new_r, new_c) not in visited and\
                (new_val <= curr_val + 1 or\
                chr(curr_val) == 'S'):
                new_paths.append(curr_path + [(new_r, new_c)])
                visited.add((new_r, new_c))

    for path in new_paths:
        queue.append(path)

    # sort queue by shortest len
    queue = collections.deque(sorted(queue, key=lambda x: len(x)))


# print(start, end)
print(steps)