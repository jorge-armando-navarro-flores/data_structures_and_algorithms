

def get_string_subsets(string):
  n = len(string)
  powerSize = 2 ** n
  for counter in range(powerSize):
    for j in range(len(string)):
      if (counter & (1 << (j)) != 0):
        print(string[j], end='')
    print()
