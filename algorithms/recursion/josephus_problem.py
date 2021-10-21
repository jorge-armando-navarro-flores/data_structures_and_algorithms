def josephus_problem(n, k, p=0):
  if n == 1:
    return 0

  return (josephus_problem(n-1, k) + k) % n
  
 

# def auxiliarFuncion(s, n, k, p=0):
#   if len(s) == 1:
#     return s[0]
#   killed = (p + (k-1)) % n
#   s.pop(killed)
#   return auxiliarFuncion(s, n-1, k, killed)
