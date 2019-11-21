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

print(factorial(120))
print(factorialLoop(120))