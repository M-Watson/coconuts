import datetime
import os
import time

i = 0
for i in range(100):
    with open('index.html','a') as f:
        string = '<meta http-equiv="refresh" content="0" /> \n <h1> %s </h1>' %str(datetime.datetime.now())
        print(string)
        f.write(string)
        time.sleep(10)
