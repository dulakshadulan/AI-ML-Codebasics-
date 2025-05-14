
import time 
import multiprocessing


def calc_square(numbers,q):
    for n in numbers:
        q.put(n*n)


if __name__=='__main__':
    arr = [1,2,3,4,5,6,7,8]
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target = calc_square, args = (arr,q))
    p1.start()

    p1.join()

    while q.empty() is False:
        print(q.get())

