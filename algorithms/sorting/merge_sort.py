# const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

# function mergeSort (array) {
#   if (array.length === 1) {
#     return array
#   }
#   // Split Array in into right and left

#   return merge(
#     mergeSort(left),
#     mergeSort(right)
#   )
# }

# function merge(left, right){

# }


# const answer = mergeSort(numbers);
# console.log(answer);
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

def mergeSort(array):
  if len(array) == 1:
    return array
  else:
    #Split Array in into right and left
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
  merged = []
  lIdx = 0
  rIdx = 0
  while lIdx < len(left) and rIdx < len(right):
    if left[lIdx] < right[rIdx]:
      merged.append(left[lIdx])
      lIdx+= 1
    else:
      merged.append(right[rIdx])
      rIdx += 1

  print(merged + left[lIdx:] + right[rIdx:])
  return merged + left[lIdx:] + right[rIdx:]

print(mergeSort(numbers))
  
