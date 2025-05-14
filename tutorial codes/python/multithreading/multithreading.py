import time
import threading


def calc_square (numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square', n**2)

def calc_cube (numbers):
    print("Calculate cube")
    for n in numbers:
        time.sleep(1)
        print("cube", n**3)

arr = [2,3,8,9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ", time.time()-t)
print("Hah... I an done with all my work now!")