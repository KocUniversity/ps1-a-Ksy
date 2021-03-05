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

def binary_search() -> None:
  global T
  global MAX_T_VAL

  min_satisfying_t = None

  left = 0
  right = MAX_T_VAL

  while left <= right:
    middle_elt = (left + right) // 2 
    result = formula_result(n, middle_elt)
    if result < B:
      left = middle_elt + 1
    else:
      min_satisfying_t = middle_elt
      right = middle_elt - 1

  T = min_satisfying_t or -1


binary_search()
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)