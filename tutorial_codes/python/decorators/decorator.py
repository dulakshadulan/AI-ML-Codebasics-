import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + "took" + str((end - start)*1000) + "mil seconds")
        return result
    return wrapper
    
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number**2)

    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number**3)
    
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)