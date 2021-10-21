def maximun_difference(arr):
  n = len(arr)
  minVal = arr[0]
  maxDifference = arr[1]- minVal
  for j in range(1, n):
    # currentNumber = arr[j]
    # currentDifference = currentNumber - minN
    # if currentDifference > maxDifference:
    #   maxDifference = currentDifference
    # if currentNumber < minVal:
    #   minVal = currentNumber
    maxDifference = max(maxDifference, arr[j] - minVal)
    minVal = min(minVal, arr[j])

  return maxDifference
