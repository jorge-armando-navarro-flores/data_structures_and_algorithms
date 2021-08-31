def simple(n):
  set_bits = 0
  while(n > 0):
    set_bits += (n & 1)
    n >> 1
  return set_bits

def Brian_and_Kerningham_algorithm(n):
  set_bits = 0
  while (n > 0):
    n = (n & (n-1))
    set_bits += 1
  return set_bits

def lookup_table(n):
  table = [None for _ in range(256)]

  def initialize():
    table[0] = 0
    #Stores the bits set of numbers from 0 - 255
    for i in range(1, 256, 1):
      table[i] = (i & 1) + table[i // 2]

  def count(n):
    # (n & 0xff) = last eight set bits of n value
    set_bits = table[n & 0xff]
    n >>= 8
    set_bits += table[n & 0xff]
    n >> 8
    set_bits += table[n & 0xff]
    n >>= 8
    set_bits += table[n & 0xff]
    n >>= 8
    return set_bits
  
  initialize()
  return count(n)

