def trapping_rain_water(arr):
  n = len(arr)
  water = 0
  lMax = [None for _ in range(n)]
  rMax = [None for _ in range(n)]
  lMax[0] = arr[0]
  for i in range(1, n):
    lMax[i] = max(arr[i], lMax[i-1])
  rMax[n-1] = arr[n-1]
  for i in reversed(range(n-1)):
    rMax[i] = max(arr[i], rMax[i+1])
  for i in range(1,n-1):
    water += (min(lMax[i], rMax[i]) - arr[i])
  # maxTower = arr[0]
  # for i  in range(1, n):
  #   if arr[i] > arr[i-1]:
  #     maxLevel = min(arr[i], maxTower)
  #     water += (maxLevel - arr[i-1]) * (i-1)
  #   if arr[i] > maxTower:
  #     maxTower = arr[i] 
  return water