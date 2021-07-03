numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(numbers):
  for i in range(len(numbers)):
    for j in range(len(numbers)-1):
      if numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers

print(bubbleSort(numbers))