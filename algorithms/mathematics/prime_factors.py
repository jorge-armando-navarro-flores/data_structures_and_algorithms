def prime_factors(n):

  if n <= 1:
    return
    
  i = 2
  while i ** 2 <= n:
    while n % i == 0:
      print(i, end=' ')
      n //= i
    i+=1
  if n > 1:
    print(n)

def prime_factors_optimized(n):
  if n <= 1:
    return
  while n % 2 == 0:
    print(2, end = ' ')
    n //= 2
  while n % 3 == 0:
    print(3, end=' ')
    n //= 3

  i = 5
  while i ** 2 <= n:
    while n % i == 0:
      print(i, end=' ')
      n //= i
    while n % (i+2) == 0:
      print(i, end=' ')
      n //= (i+2)
    i+=6
  if n > 1:
    print(n)