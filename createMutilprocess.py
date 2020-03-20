#!/usr/bin/env python3

import multiprocessing as mp
import time

def worker(name):
    print(name)
    time.sleep(3)

p1 = mp.Process(target=worker, args=('frank',))
p2 = mp.Process(target=worker, args=('jack',))
p1.start()
p2.start()
p1.join()
p2.join()

print('done...')

