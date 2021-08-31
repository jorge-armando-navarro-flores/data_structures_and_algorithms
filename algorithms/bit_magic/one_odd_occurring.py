def get_one_odd_occurring(arr):
  one_odd_occurring = 0
  for number in arr:
    one_odd_occurring = one_odd_occurring ^ number
  return one_odd_occurring

def find_missing_no(arr):
  missing = 0
  n = 1
  for i in range(len(arr)):
    missing ^= arr[i]
    n ^= (i+2)

  return n ^ missing
