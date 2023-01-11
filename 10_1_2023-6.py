def createList(*args):
    newList = []
    for i in args:
        newList.append(i)
    return newList

def createTuple(*args):
    newTuple = []
    for i in args:
        newTuple.append(i)
    return tuple(newTuple)

myList = createList(1, 2, 3)
myTuple = tuple(myList)
print('Tuple', myTuple)
myTuple = createTuple(4, 5, 6)
myList = list(myTuple)
print('List', myList)
