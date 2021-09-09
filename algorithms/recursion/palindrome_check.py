def palindrome_check(string, l=0):
  r = len(string) -1 - l
  if l >= r:
    return True

  return string[l] == string[r] and palindrome_check(string, l+1)
