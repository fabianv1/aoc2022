from functools import cmp_to_key

#############################
###    HELPER FUNCTIONS   ###
#############################

def to_nested_list(str_list):
    """
    str_list : string representation of python list object
    """
    # base case of flat list
    if str_list.count('[') == 1:
        int_list = str_list[1:-1].split(',')
        if int_list == ['']:
            return []
        return [int(x) for x in int_list]
    
    # recursive case of nested lists
    result = []
    i = 1
    while i < len(str_list)-1:
        char = str_list[i]
        if char == '[': # nested list found, must make recursive call
            start, stack = i,  ['[']
            i += 1
            while stack and i < len(str_list)-1: # find closing bracket of nested list
                curr = str_list[i]
                if curr == '[': # account for deeper nesting by finding bracket pairs
                    stack.append(curr)
                if curr == ']':
                    stack.pop()
                i += 1

            result.append(to_nested_list(str_list[start:i]))
        elif char != ',':
            j = i+1
            str_int = char
            while str_list[j] not in [',', ']']: # get entire number, not just first digit
                str_int += str_list[j]
                j += 1
            result.append(int(str_int))
        i += 1
    
    return result

def convert_to_python(pair):
    left, right = pair
    if left[0] == '[': # list
        left = to_nested_list(left)
    else:
        left = int(left)
    
    if right[0] == '[': # list
        right = to_nested_list(right)
    else:
        right = int(right)
    
    return left, right


file = open("input13.txt", 'r').read().split('\n\n')
pairs = [convert_to_python(x.strip().split('\n'))
             for x in file]

def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        return -1 if left < right else 1
    
    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            if l == r:
                continue
            result = check_order(l, r)
            if result != 0:
                return result
        if len(left) == len(right):
            return 0
        return  -1 if len(left) < len(right) else 1

    if isinstance(left, int) and isinstance(right, list):
        left = [left]
        return check_order(left, right)
    
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
        return check_order(left, right)
    
    assert(False)


### part 1
ans1 = 0
for i, pair in enumerate(pairs):
    if check_order(*pair) == -1:
        ans1 += i+1
print(ans1)

### part 2
lines = [x[0] for x in pairs] + [x[1] for x in pairs] + [[[2]]] + [[[6]]]
lines.sort(key=cmp_to_key(check_order))
ans2 = (lines.index([[2]])+1) * (lines.index([[6]])+1)
print(ans2)
