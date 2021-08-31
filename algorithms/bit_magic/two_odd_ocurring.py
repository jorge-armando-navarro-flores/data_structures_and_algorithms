def get_two_odd_ocurring(arr):
  xor = 0
  group1 = 0
  group2 = 0
  # get xor of array
  for number in arr:
    xor ^= number

  # right most set bit of xor
  rmsb = xor & ~(xor - 1)

  for number in arr:
    # rmsb bit is set in number
    if number & rmsb != 0:
      group1 ^= number
    else:
      group2 ^= number

  return [group1, group2]
