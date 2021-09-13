def generate_subsets(string, sub= "", N = 0):
  if N == len(string):
    print(sub, end=' ')
    return
  
  generate_subsets(string, sub, N+1)
  generate_subsets(string, sub + string[N], N+1)

