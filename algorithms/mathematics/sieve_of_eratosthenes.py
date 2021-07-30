def sieve_of_eratosthenes(n):
  isPrime =[True for _ in range(n+1)]
  i = 2
  while i*i <=n:
    if isPrime[i]:
      for j in range(i*i, n+1, i):
        isPrime[j] = False
    i += 1

  for i in range(2, n+1, 1):
    if isPrime[i]:
      print(i, end=' ')

def sieve_of_eratosthenes_optimized(n):
  isPrime =[True for _ in range(n+1)]

  for i in range(2, n+1):
    if isPrime[i]:
      print(i , end=' ')
      for j in range(i*i, n+1, i):
        isPrime[j] = False

def primes_before_a_number(n):
  if n > 3:
    print(2, 3, end =' ')
  elif n > 2:
    print(2, end=' ')

  for i in range(5, n, 6):
    print(i, i+2, end=' ')

  if(i + 6 <= n):
    print(i+6, end=' ')