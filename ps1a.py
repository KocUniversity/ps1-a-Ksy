n, B = list(map(int, input().strip().split()))
T = 0

# your code here
MAX_T_VAL = 10000

def formula_result(n:int, t:int) -> int:
  result = 0
  for i in range(1,n+1):
    if i % 2 == 0:
      result += ((2**i + 1)**(n - i)) * t
    else:
      result += ((3**i + 1)**(n - i)) * t
    
  return result

def bf_search() -> None:
  global T
  temp_t = 1
  t_is_valid = False

  while temp_t < MAX_T_VAL:
    result = formula_result(n, temp_t)
    if result < B:
      temp_t += 1
    else:
      t_is_valid = True
      break
    
  if t_is_valid:
    T = temp_t
  else:
    T = -1

bf_search()
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)