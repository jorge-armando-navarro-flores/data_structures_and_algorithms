def max_consecutive_1s(arr):
  n = len(arr)
  maxConsecutive = 0
  currentConsecutive = 0
  for i in range(n):
    if arr[i] == 1:
      currentConsecutive += 1
    else:
       currentConsecutive = 0
    if currentConsecutive > maxConsecutive:
      maxConsecutive = currentConsecutive
     
  return maxConsecutive