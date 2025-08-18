# A decorator is a function that takes another function (or method) as an argument and returns a new 
# function that typically extends or alters the behavior of the original function.

# Decorators, Generators, Iterators, @staticmethod, @classmethod, @property, Regular Expressions (Regex).

'''
def decorator_func(say_hello):
    def wrapper():
        print("Before func runs..")
        say_hello()
        print("After function runs..")
    return wrapper

@decorator_func
def say_hello():
    print("hi")

say_hello()
'''



#decorator with arguments


'''
def debug(func):
    def wrapper(*args,**kwargs):
        print(f"Function : {func.__name__} calling with {args} , {kwargs}")
        result = func(*args,**kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a,b):
    return a+b

add(4,6)

'''


#Stacking multiple decorators

'''def uppercase(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper

def exclaim(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)+"!!!"
    return wrapper

@uppercase
@exclaim
def greet():
    return "Akshay"

print(greet())
print(greet.__name__)'''


# wraps Without wraps, the decorated function loses its metadata (__name__, __doc__).

'''from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

@debug
def say_hi():
    return "hi"

print(say_hi())'''



'''

📝 Easy

Write a decorator that prints "Function started" and "Function ended" before and after any function.

Create a decorator that measures the execution time of a function.

'''

import time

def decorator(func):
    def wrapper():
        start = time.time()
        print("Function Started")
        result =  func()
        print(f"Time taken {time.time() - start}")
        print("Function ended")
        return result
    return wrapper

@decorator
def say():
    return "say..."

print(say())


'''

📝 Medium

Write a decorator that logs arguments and return values of any function.

Create a decorator @only_ints that raises an error if the function is called with non-integer arguments.

📝 Hard

Create a decorator @retry(n) that retries a function call n times if it raises an exception.

Create a class-based decorator @count_calls that counts how many times a function was called.

'''
