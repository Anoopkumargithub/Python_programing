from email.utils import localtime
from threading import local
import time

initial = time.time()
print(initial)
k = 0
while (k<45) :
    print("This is Anoop")
    localtime = time.sleep(2)
    k +=1
    print("while loop ran in", time.time() - initial, "seconds")

    initial2 = time.time()
for i in range(45) :
    print("This is Anoop")
    print("forv loop ran in", time.time() - initial2, "seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
