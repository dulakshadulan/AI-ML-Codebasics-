import time
import threading


def calc_square(numbers):
    print("calculate square of numbers : ")
    for n in numbers:
        time.sleep(0.2)
        print('square: ', n**2)


def calc_cube(numbers):
    print("calculate cube of numbers : ")
    for n in numbers:
        time.sleep(0.2)
        print('cube: ', n**3)

if __name__=='__main__':
    array = [1,2,3,4,5]

    t = time.time()

    t1  = threading.Thread(target=calc_square,args=(array,))
    t2  = threading.Thread(target=calc_cube,args=(array,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done in : ", time.time() - t)
    print("Hah... I am done all my work now!")