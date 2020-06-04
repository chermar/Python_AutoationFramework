import inspect

def whomai():
    return inspect.stack()[1][3]

def Myfun():
    x=whomai()
    print(x)

Myfun()