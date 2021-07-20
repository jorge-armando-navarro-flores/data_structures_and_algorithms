def greatest_common_divider(a, b):
  while(a != b):
    if a > b:
      a -= b
    else:
      b -= a
  return a

def greatest_common_divider_optimized(a, b):
  if b == 0:
    return a
  else:
    return greatest_common_divider_optimized(b, a%b)

print(greatest_common_divider_optimized(4, 6))


