def maximum_circular_sum_subarray(arr):
  n = len(arr)
  maxEnding = arr[0]
  maxSum = arr[0]
  for i in range(1,n):
    maxEnding = max(maxEnding + arr[i], arr[i])
    if maxEnding > maxSum:
      maxSum = maxEnding

  maxCircularEnding = maxSum
  maxCircularSum = maxSum
  for i in range(n-1):
    print(maxCircularEnding)
    maxCircularEnding = max(maxCircularEnding + arr[i], arr[i])
    if maxCircularEnding > maxCircularSum:
      maxCircularSum = maxCircularEnding
  return max(maxSum, maxCircularSum)
  return maxCircularSum