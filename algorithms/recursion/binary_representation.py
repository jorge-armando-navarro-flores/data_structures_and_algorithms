def binary_representation(n):
  if n == 0:
    return
  binary_representation(n//2)
  print(n % 2, end='')