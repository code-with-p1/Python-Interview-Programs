import monkey

def monkey_func(self):
    print ("monkey_func() is called")

# replacing address of "func" with "monkey_func"
monkey.A.func = monkey_func
obj = monkey.A()

# calling function "func" whose address got replaced
# with function "monkey_func()"
obj.func()