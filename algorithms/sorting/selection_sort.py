numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(numbers):
  length = len(numbers)
  smallestIdx = 0
  for i in range(length-1):
    for j in range(i + 1, length):
      if numbers[j] < numbers[smallestIdx]:
        smallestIdx = j

    numbers[i], numbers[smallestIdx] = numbers[smallestIdx], numbers[i]
  return numbers

print(selection_sort(numbers))
