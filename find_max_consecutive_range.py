
from itertools import groupby
from operator import itemgetter

def find_max_consecutive_range(arr):
  a= []
  y = []

  for k,g in groupby(enumerate(arr), lambda  x:x[0]-x[1]):
    b = (map(itemgetter(1), g))
    b = list(map(int,b))
    a.append((b[0],b[-1]))

  for ele in a:
    y.append(len(ele))

  length = 0
  for ele in a:
    if len(ele) > length:
      s = len(ele)
      length , s = s ,length

  q = (a[y.index(length)])
  return [q[0],q[-1]]


if __name__ == '__main__':
  # arr = [1, 11, 3, 0, 15, 5, 5, 2, 4, 10, 7, 12, 6]
  arr = [11, 7, 3, 4, 2, 1, 0]
  arr.sort()
  arr = set(arr)
  print(find_max_consecutive_range(arr))
