def f(x, y):
    if y <= x: f(x-y, y) + 1
    print(x, y)

f(200, 100)
