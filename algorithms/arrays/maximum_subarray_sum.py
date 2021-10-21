def maximum_subarray_sum(arr):
  n = len(arr)
  maxEnding = arr[0]
  maxSum = arr[0]
  for i in range(1,n):
    maxEnding = max(maxEnding + arr[i], arr[i])
    if maxEnding > maxSum:
      maxSum = maxEnding
  return maxSum