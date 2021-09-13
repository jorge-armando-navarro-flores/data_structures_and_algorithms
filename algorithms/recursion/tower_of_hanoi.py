def tower_of_hanoi(n, a, b, c):
  if n == 0:
    return
  
  tower_of_hanoi(n-1, a, c, b)
  print(f"Move disc {n} from {a} to {c}")
  tower_of_hanoi(n-1, b, a, c)
