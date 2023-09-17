# lambda x: x + 2
def add(x): return x + 2
# lambda x,y: x + y
def sum(x, y): return x + y


print(add(3))
print(sum(2, 4))


# ----------------------------------------------
def funcBuilder(x):
    return lambda num: num * x if type(num) == int else "Not a number"


doTen = funcBuilder(10)
doTwenty = funcBuilder(20)

print(doTen(2))
print(doTwenty(2))
