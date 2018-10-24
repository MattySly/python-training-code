# a collection of instructions
# a collection of code


def function1():
    print("ahhh")
    print("ahhh 2")
print("this is outside function")
function1()

# a mapping
# input or an argument
def function2(x):
    return 2*x

a = function2(3)
# return value (so function2 = 3, and the return is 2*3 which equals 6. so a = 6)
print(a)

b = function2(4)
print(b)

c = function2() #returns an error because it's blank

def function3(x, y):
    return x + y
e = function3(1, 2)
print(e)