def insert(arr, x, pos):
  idx = pos-1

  i = len(arr) - 2
  while i >= idx:
    arr[i+1] = arr[i]
    i-= 1

  arr[idx] = x
  return arr
