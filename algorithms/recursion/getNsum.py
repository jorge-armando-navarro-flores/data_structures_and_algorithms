def getNsum(n):
  if n == 0:
    return 0
  else:
    return n + getNsum(n-1)