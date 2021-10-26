def maximum_circular_sum_subarray(arr):
  n = len(arr)
  max_normal = maximum_subarray_sum(arr)
  if max_normal < 0:
    return max_normal
  arr_sum = 0
  for i in range(n):
    arr_sum += arr[i]
    arr[i] = -arr[i]
  max_circular = arr_sum + maximum_subarray_sum(arr)
  return max(max_normal, max_circular)

def maximum_subarray_sum(arr):
  n = len(arr)
  maxEnding = arr[0]
  maxSum = arr[0]
  for i in range(1,n):
    maxEnding = max(maxEnding + arr[i], arr[i])
    if maxEnding > maxSum:
      maxSum = maxEnding
  return maxSum 
  