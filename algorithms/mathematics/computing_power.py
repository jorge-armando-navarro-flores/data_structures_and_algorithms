def computing_power_recursive(x, n):
  if n == 0:
    return 1

  temp = computing_power_recursive(x, n//2)
  temp = temp * temp
  if n % 2 == 0:
    return temp
  else:
    return temp * x


def computing_power_iterative(x, n):
  suv = 1
  while(n > 0):
    if(n % 2 != 0):
      suv *= x
    else:
      x *= x
    n //= 2
  return suv
