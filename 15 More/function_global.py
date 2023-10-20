x = 50 #gloabl variable is defined


def func():
    global x #assign global value

    print('Global x is', x)
    x = 2
    print('Changed global x to', x,'making it local')


func()
print('Value of x is', x)
