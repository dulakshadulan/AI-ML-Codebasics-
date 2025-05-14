
import time 
import multiprocessing


def calc_square(numbers,result,v):
    print("calculate square of numbers : ")
    for idx,n in enumerate(numbers):
        print('square: ', n**2)
        result[idx] = n**2
        v.value += n**2


if __name__=='__main__':
    arr = [1,2,3,4,5,6,7,8]

    #shared memory variables
    result = multiprocessing.Array('i',8)

    v = multiprocessing.Value('d',0.0)

    p1 = multiprocessing.Process(target = calc_square, args = (arr,result,v))
    p1.start()

    p1.join()
    print(result[:])
    print(v.value)
