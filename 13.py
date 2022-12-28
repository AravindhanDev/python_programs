def printFloat(floatValue):
    print('{:.2f}'.format(floatValue))
    if floatValue > 0: print('+{:.2f}'.format(floatValue))
    else: print('-{:.2f}'.format(floatValue))
    print(int(floatValue))

printFloat(3.14157899)
