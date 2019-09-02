import time
import kthread
from colorama import init, Fore, Back

init()

def circle1(diameter):
    print('\r')
    print(Fore.MAGENTA + ' Thread through calculating the Circumference of Circle ', '\r')
    print('\r')
    for d in diameter:
        time.sleep(1.75)
        print(Fore.MAGENTA +' Circumference: ', d * 3.14, '\r')
       # print('\r')

def circle2(radius):
    print(Fore.CYAN + ' Thread through calculating the Area of a Circle ', '\r')
    print('\r')
    for r in radius:
        time.sleep(1.75)
        print(Fore.CYAN + ' Area: ', r * r * 3.14,'\r')
      # print('\r')

arr = [10,11,12,13,14,15]

t = time.time()

t1 = kthread.KThread(target=circle1, args =(arr, ))
t2 = kthread.KThread(target=circle2, args =(arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

print('\r')
print(Fore.YELLOW + 'KThreading terminated in: ', time.time())
print('\r')

