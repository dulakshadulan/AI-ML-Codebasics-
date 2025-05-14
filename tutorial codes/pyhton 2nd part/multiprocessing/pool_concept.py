from multiprocessing import Pool
import time

def f(arr):
    sum = 0
    for x in range(100000):
        sum += x*x
    return sum

if __name__=='__main__':
    t1 = time.time()
    p = Pool(processes=3)
    result = p.map(f,range(10000))
    p.close()
    p.join()


    print("pool took", time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))
    print("serial processing took",time.time()-t2)


