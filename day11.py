inputfile = [x.strip().split('\n') for x in open("input11.txt", 'r').read().split('\n\n')]

# example = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""

# inputfile = [x.strip().split('\n') for x in example.split('\n\n')]

ROUNDS = 10000
MOD = 1
monkeys = {}

for m in inputfile:
  monkey_id, items, operation, test, true_cond, false_cond = m
  monkey_id = int(monkey_id[:-1].split()[1])
  monkeys[monkey_id] = {
    'items': [int(x) for x in items.split(': ')[1].split(', ')],
    'operation': operation.split(': ')[1],
    'test': int(test.split()[3]),
    'true': int(true_cond.split()[5]),
    'false': int(false_cond.split()[5]),
    'count': 0
  }
  MOD *= monkeys[monkey_id]['test'] # part 2

for r in range(ROUNDS):
  print('Round', r)
  for id in sorted(monkeys.keys()):
    m = monkeys[id]
    while m['items'] != []:
      old = m['items'].pop(0)
      new = None
      exec(m['operation'])
      new %= MOD
      if new % m['test'] == 0:
        monkeys[m['true']]['items'].append(new)
      else:
        monkeys[m['false']]['items'].append(new)
      m['count'] += 1
      
monkey_businesses = []
for k,v in monkeys.items():
  monkey_businesses.append(v['count'])

top1, top2 = sorted(monkey_businesses, reverse=True)[:2]
print(top1, top2)
print('shenanigans:', top1*top2)