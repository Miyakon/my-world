# -*- coding: utf-8 -*-

def print_q(target: str, middle: str, q_cnt: int = 0) -> int:
  print(f'? {target} {middle}')
  return q_cnt + 1

n, q = map(int, input().split())
sorting = ['A']
q_cnt = 0

# If the test set is 3
if n==5:
  light = []
  heavy = []
  for cnt in range(0, n-1):
    X = sorting[0]
    Y = chr(ord(sorting[0]) + cnt)
    print_q(X, Y)
    result = input()
    if result == '<':
      light.append(X)
      heavy.append(Y)
    else:
      light.append(Y)
      heavy.append(X)
  light_counter = {char: light.count(char) for char in light}
  heavy_counter = {char: heavy.count(char) for char in heavy}
  most_light = [k for k, v in light_counter.items() if v == 2]
  most_heavy = [k for k, v in light_counter.items() if v == 2]
  target_index = 0

  # Identify the lightest value
  if len(most_light) == 2:
    X, Y = most_light
    print_q(X, Y)
    result = input()
    if result == '<':
      target_index = 0
    elif result == '>':
      target_index = 1
  elif len(most_light) == 1:
    target_index = 0
  sorting[0] = most_light[target_index]

  # Identify the heaviest value
  if len(most_heavy) == 2:
    X, Y = most_heavy
    print_q(X, Y)
    result = input()
    if result == '<':
      target_index = 1
    elif result == '>':
      target_index = 0
  elif len(most_heavy) == 1:
    target_index = 0
  sorting[4] = most_heavy[target_index]

else:
  # binary search
  for cnt in range(1, n):
    low = 0 # light(left)
    high = len(sorting) - 1 # heavy(right)
    mid = (low + high) // 2
    
    target = chr(ord(sorting[0]) + cnt)

    while(True):
      add_index: int = None
      q_cnt = print_q(target, sorting[mid], q_cnt=q_cnt)
      result = input()

      #　binary search like
      if low == high:
        if result == '<':
          add_index = mid
        elif result == '>':
          add_index = mid + 1

      elif low == mid:
        if result == '<':
          add_index = mid
        elif result == '>':
          low = high
      
      else:
        if result == '<':
          high = mid - 1
        elif result == '>':
          low = mid + 1

      # insert list
      if add_index is not None:
        if add_index == len(sorting):
          sorting.append(target)
        else:
          sorting.insert(add_index, target)
        break
      
      mid = (low + high) // 2

  # output result
  sort_str = ''.join(sorting)
  ans = '! ' + sort_str
  print(ans, flush=True)
  print(f'q_cnt : {q_cnt}')