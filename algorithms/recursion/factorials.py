# // Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

def findFactorialRecursiveTail(n, k=1):
  if n == 0 or n == 1:
    return k;
  else:
    return findFactorialRecursiveTail(n-1, k*n) 

def findFactorialRecursive(n, k=1):
  if n == 0:
    return 1;
  else:
    return n * findFactorialRecursive(n-1) 

