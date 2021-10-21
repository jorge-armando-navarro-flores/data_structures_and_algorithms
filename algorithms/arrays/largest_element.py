def largest_element(arr):
  largestIdx = 0
  for i in range(len(arr)):
    if arr[i] > arr[largestIdx]:
      largestIdx = i
  return largestIdx
