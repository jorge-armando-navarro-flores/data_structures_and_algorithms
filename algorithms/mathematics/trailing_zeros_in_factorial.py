def trailing_zeros_in_factorial(n):
  """
  T - O(logN)
  """
  trailing_zeros = 0
  five_pow = 5
  while five_pow <= n:
    trailing_zeros +=  n // five_pow
    five_pow *= 5


  return trailing_zeros


print(trailing_zeros_in_factorial(100))
