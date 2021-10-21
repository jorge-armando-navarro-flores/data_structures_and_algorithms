def left_rotate_array_by_d(arr, d):
  n = len(arr)
  # temp = [None for _ in range(d)]
  # for i in range(d):
  #   temp[i] = arr[i]
  # for i in range(d, n):
  #   arr[i-d] = arr[i]
  # for i in range(d):
  #   arr[n-d+i] = temp[i]
  reverse(arr, 0, d-1)
  reverse(arr, d, n-1)
  reverse(arr, 0, n-1)
  
  
  return arr

def reverse(arr, low, high):
  while(low < high):
    swap(low, high, arr)
    low += 1
    high -= 1

def swap(i, j, arr):
  arr[i], arr[j] = arr[j], arr[i]
