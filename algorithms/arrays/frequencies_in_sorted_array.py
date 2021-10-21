def frequencies_in_sorted_array(arr):
  n = len(arr)
  freq = 0
  val = arr[0]
  for i in range(n):
    if arr[i] == val:
      freq += 1
    else:
      print(val, freq)
      val = arr[i]
      freq = 1

  print(val, freq)
