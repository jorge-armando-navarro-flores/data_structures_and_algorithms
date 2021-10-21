def leaders_in_array(arr):
  n = len(arr)
  leader = arr[n-1]
  print(leader, end=' ')
  for i in reversed(range(1, n-1)):
    if arr[i] > leader:
      leader = arr[i]
      print(leader, end=' ')
      
