def all_divisors_of_a_number(n):
  i = 1
  while i ** 2 <=n:
    if n % i == 0:
      print(i)
      if i != n / i:
        print(f"{n / i:2.0f}")
    i += 1

def all_divisors_of_a_number_ordered(n):
  i = 1
  while i ** 2 < n:
    if n % i == 0:
      print(i, end=' ')
    i += 1
  while i >= 1:
    if n % i == 0:
      print(f"{n / i:2.0f}", end = ' ')
    i -= 1