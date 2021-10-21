def buy_and_sell_problem(price):
  n = len(price)
  profit = 0
  for i in range(1, n):
    if price[i] > price[i-1]:
      profit += (price[i] - price[i-1])
  return profit
  # maxProfit = 0
  # i = 0
  # while i < n:
  #   j = i
  #   while j < n-1 and arr[j+1] > arr[j]:
  #     j += 1
  #   maxProfit += (arr[j] - arr[i])
  #   i = j+1
  # return maxProfit
