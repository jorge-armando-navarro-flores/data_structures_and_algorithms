from algorithms.mathematics.greatest_common_divider import greatest_common_divider_optimized

def least_common_multiple(a, b):
  return (a*b) // greatest_common_divider_optimized(a,b)



