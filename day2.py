input = open("input2.txt", 'r').readlines()

scores = {
  'A X': 3 + 1,
  'A Y': 6 + 2,
  'A Z': 3,
  'B X': 1,
  'B Y': 3 + 2,
  'B Z': 6 + 3,
  'C X': 6 + 1,
  'C Y': 2,
  'C Z': 3 + 3
}

mapping = {
  'X': {
    'A': 'A Z',
    'B': 'B X',
    'C': 'C Y',
  },
  'Y': {
  'A': 'A X',
  'B': 'B Y',
  'C': 'C Z'
  },
  'Z': {
  'A': 'A Y',
  'B': 'B Z',
  'C': 'C X'
  }
}

total = 0
total2 = 0
for i in input:
  total += scores[i.strip()]
  total2 += scores[mapping[i[2]][i[0]]]

print(total)
print(total2)