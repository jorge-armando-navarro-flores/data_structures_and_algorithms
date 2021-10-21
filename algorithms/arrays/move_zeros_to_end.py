def move_zeros_to_end(arr):
  n = len(arr)
  count = 0
  for i in range(n):
    if arr[i] != 0:
      swap(i, count, arr)
      count += 1
  return arr

def swap(i, j, arr):
  arr[i], arr[j] = arr[j], arr[i]