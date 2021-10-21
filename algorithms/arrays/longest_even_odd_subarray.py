def longest_even_odd_subarray(arr):
  n = len(arr)
  longest = 1
  curr = 1
  for i in range(1, n):
    if arr[i] % 2 != arr[i-1] % 2:
      curr += 1
      longest = max(longest, curr)
    else:
      curr = 1
  return longest