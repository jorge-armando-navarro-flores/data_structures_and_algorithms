# // Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

def findFactorialRecursive(number):
  if number == 1:
    return 1;
  else:
    return number * findFactorialRecursive(number-1) 



print(findFactorialRecursive(5))
