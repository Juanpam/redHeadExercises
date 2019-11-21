# Always define both conditions: inductive and stop condition
def factorial(x):
    if(x == 1): return 1
    else: return factorial(x-1) * x

def factorialLoop(x):
    result = 1
    while(x != 1):
        result *= x
        x-=1
    return result

def gfactorial(n):
  if n >= 1 :
    return n*factorial(n-1)
  else :
    return 1

def gloopfactorial(n):
  x = 1
  for i in range(1,n+1):
    x *= i
  return x

print(factorial(120))
print(factorialLoop(120))