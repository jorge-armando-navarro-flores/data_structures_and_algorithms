numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(numbers):
  length = len(numbers)
  for i in range(1, length):
    j = i
    while numbers[j] < numbers[j-1] and j > 0:
      numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
      j -= 1
  return numbers

print(insertion_sort(numbers))
