import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s')
def add (x,y):
    return x+y

def subttract (x,y):
    return x - y

def divide(x,y):
    return x / y


x = 10
y = 20

py_add = add(x,y)
logging.debug('watch out!')
# ('Add : {} + {} = {}'.format(x, y, py_add))

py_subtract = subttract(x,y)
logging.debug('Subtact: {} - {} = {}'.format(x, y, py_subtract))