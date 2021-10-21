def delete(arr,n, x):
  idx  = 0 
  while idx < len(arr):  
    if arr[idx] == x:
      break
    idx += 1

  if idx == n:
    return n

  for j in range(idx, n-1):
    arr[j] = arr[j+1]

  return arr