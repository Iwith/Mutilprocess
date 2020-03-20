#!/usr/bin/env python

import multiprocessing as mp
import time, random

def write_worker(queue,name):
    print('I am ',name)
    queue.put(name)
    time.sleep(random.random())

def read_worker(queue,name):
    print('I am ',name)
    value = queue.get()
    print('get-value:',value)

q = mp.Queue()
pw = mp.Process(target=write_worker, args=(q, 'frank',))
pr = mp.Process(target=read_worker, args=(q, 'jack',))
pw.start()
pr.start()
pw.join()
pr.terminate()  # pr不能用join，否则会一直等待
print('end...')
