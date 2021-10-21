def linear_search(arr, target):
  for element in arr:
    if element == target:
      return target
  return -1