def second_largest_element(arr):
  secondLargestIdx = -1
  largestIdx = 0
  
  for i in range(len(arr)):
    
    if arr[i] > arr[largestIdx]:
      secondLargestIdx = largestIdx
      largestIdx = i
    elif arr[i] != arr[largestIdx]:
      if secondLargestIdx == -1 or arr[i] > arr[secondLargestIdx]:
        secondLargestIdx = i      
  
  return secondLargestIdx
  