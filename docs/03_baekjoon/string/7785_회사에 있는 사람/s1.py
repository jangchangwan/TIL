import sys

dict_table = dict()

for _ in range(int(sys.stdin.readline())):
  p, c = sys.stdin.readline().rstrip().split()

  if c == 'enter':
    dict_table[p] = 'enter'
  else:
    if dict_table[p]:
      del dict_table[p]

for people in sorted(dict_table, reverse=True):
  print(people)