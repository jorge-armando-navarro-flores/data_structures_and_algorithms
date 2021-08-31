
def check_kth_is_set(n , k):
  if(n & (1 << (k-1)) != 0):
    return True
  else:
    return False
