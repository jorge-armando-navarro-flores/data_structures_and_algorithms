def subset_sum(numbers, n, sum):
  if n == 0:
    return 1 if sum == 0 else 0

  return subset_sum(numbers, n-1, sum) + subset_sum(numbers, n-1, sum - numbers[n-1])
  
 