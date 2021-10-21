def remove_duplicates_sorted_array(arr):
  n = len(arr)
  size = 1
  for i in range(1, n):
    if arr[size-1] != arr[i]:
      arr[size] = arr[i]
      size += 1
  
  return size