
def count_digits(x):
  digit_number = 0
  while x > 0:
    digit_number += 1
    x //= 10
  return digit_number

print(count_digits(3215))


