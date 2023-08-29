def zero(operation = None): return 0 if not operation else operation(0)#your code here
def one(operation = None): return 1 if not operation else operation(1)#your code here
def two(operation = None): return 2 if not operation else operation(2)#your code here
def three(operation = None): return 3 if not operation else operation(3)#your code here
def four(operation = None): return 4 if not operation else operation(4)#your code here
def five(operation = None):return 5 if not operation else operation(5) #your code here
def six(operation = None): return 6 if not operation else operation(6)#your code here
def seven(operation = None): return 7 if not operation else operation(7)#your code here
def eight(operation = None): return 8 if not operation else operation(8)#your code here
def nine(operation = None):return 9 if not operation else operation(9) #your code here

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y #your code here
def times(y): return lambda x: x*y #your code here
def divided_by(y): return lambda x: x/y #your code here

print(zero(times(one())))