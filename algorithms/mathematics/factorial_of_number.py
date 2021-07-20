def factorial_of_number_iterative(n):
  factorial = 1
  for number in range(2, n+1):
    factorial = factorial * number
  return factorial

def factorial_of_number_recursive(n):
  if n == 0:
    return 1
  else:
    return n * factorial_of_number_recursive(n-1)

print(factorial_of_number_iterative(25))