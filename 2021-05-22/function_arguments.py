# argument, parameters

def greeting(name, time):
    print("hello", name, time)


# call a function
# greeting('Tom')
# greeting(name='Tom', time='2021')


# return
# input -> output
# help, document

def add(x, y):
    """
    This function can be used to caculate the sum of x and y
    :param x: the frist number, type is integer
    :param y: the second number, type is integer
    :return: will return c, which is the sum of x and y
    """
    c = x + y
    return c

add(10, 2)
