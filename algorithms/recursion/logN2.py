def logN2(n):
  if n == 1:
    return 0
  else:
    return 1 + logN2(n//2)