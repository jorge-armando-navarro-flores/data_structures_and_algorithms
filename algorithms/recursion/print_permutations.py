def print_permutations(s, i=0):
  if(i == len(s)):
    print(s, end=' ')
    return

  for j in range(i, len(s)):
    swap(i, j, s)
    print_permutations(s, i+1)
    swap(i, j, s)



def swap(i, j, s):
  s[i], s[j] = s[j], s[i]

