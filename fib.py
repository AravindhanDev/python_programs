# iterative way

'''
def fib(n):
    n1 = 0
    n2 = 1
    print(n1, n2, end=" ")

    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2
        n2 = n3

n = int(input("enter range "))
fib(n)
'''

# recursive way

def fib(n1, n2, n):
    if n == 0: return
    if n1 == 0: print(n1, n2, end=" ")
    print(n1 + n2, end=" ")
    fib(n2, n1 + n2, n-1)

n = int(input("Enter range "))
fib(0, 1, n)
    
