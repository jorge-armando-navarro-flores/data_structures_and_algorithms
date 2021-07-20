def palindrome_number(n):
  """
  Complexity:
    Time: O(d)
      d = Number of digits
    Space: O(1)

  """
  reversedNumber = reverseNumber(n)
  return n == reversedNumber

def reverseNumber(n):
  reversedNumber = 0
  number = n
  while number > 0:
    lastDigit = number % 10
    reversedNumber = reversedNumber * 10 + lastDigit
    number //= 10
  return reversedNumber

print(palindrome_number(71717))

