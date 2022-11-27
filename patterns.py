'''
print()
for i in range(1, 6):
    if i == 1 or i == 5:
        for k in range(1, 6):
            print("*", end='   ')
        print("\n")
    else:
        for j in range(1, 6):
            if j == 1 or j == 5:
                print("*", end='   ')
            else:
                print(" ", end='   ')
        print("\n")
print()
'''

'''
print()

for i in range(1, 6):
    if i == 1 or i == 5:
        for k in range(1, 6):
            if k == 1 and i == 1:
                print("$", end='   ')
            elif k == 5 and i == 5:
                print("$", end='   ')
            else:
                print("*", end='   ')
        print("\n")
    else:
        for j in range(1, 6):
            if j == 1 or j == 5:
                print("*", end='   ')
            else:
                if i == 2 and j == 2:
                    print("$", end='   ')
                elif i == 3 and j == 3:
                    print("$", end='   ')
                elif i == 4 and j == 4:
                    print("$", end='   ')
                else:
                    print(" ", end='   ')
        print("\n")

print()
'''


'''
print()

for i in range(1, 6):
    if i == 1 or i == 5:
        for k in range(1, 6):
            if k == 1 or k == 5:
                print("$", end='   ')
            else:
                print("*", end='   ')
        print("\n")
    else:
        for j in range(1, 6):
            if j == 1 or j == 5:
                print("*", end='   ')
            else:
                if i == 2 and j == 2 or i == 2 and j == 4:
                    print("$", end='   ')
                elif i == 3 and j == 3:
                    print("$", end='   ')
                elif i == 4 and j == 4 or i == 4 and j == 2:
                    print("$", end='   ')
                else:
                    print(" ", end='   ')
        print("\n")

print()
'''

'''
print()

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end='  ')
    print("\n")


for i in range(1, 6):
    for k in range(5, i, -1):
        print("*", end='  ')
    print("\n")

print()
'''

'''
print()

for i in range(1, 4):
    for k in range(3, 1, -1):
        if i == 1: break
        if i == 2 and k == 3: continue
        print(k, end=" ")
    for j in range(0, i):
        print(j+1, end=" ")
    print("\n")

print()
'''

