def rope_cutting_problem(n, a, b, c):
  if n == 0:
    return 0
  if n < 0: 
    return -1
  maxPieces = max(
                  rope_cutting_problem(n-a, a, b, c),
                  rope_cutting_problem(n-b, a, b, c),
                  rope_cutting_problem(n-c, a, b, c)
                )
  if maxPieces == -1:
    return -1
  return maxPieces + 1