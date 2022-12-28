# no arguments
'''
def run(arg):
    print(arg)

run()
'''

# keyword arguments

'''
def run(arg):
    print(arg)

run(arg="Hello")
'''

# default arguments

'''
def run(arg="Hello"):
    print(arg)

run()
'''

#variable length arguments

'''
def run(*args):
    for i in args:
        print(i, end=" ")

run(10, 20, 30)
'''





