import multiprocessing as mp
import time


def worker(shared, name, lock):
    print(name)
    lock.acquire()
    for i in range(10):
        shared.value += 3
        time.sleep(0.1)
        print('sum-1',shared.value)
    lock.release()  # 整个for 循环结束后才释放锁

def job(shared, name, lock):
    print(name)
    lock.acquire()
    for i in range(10):
        shared.value = shared.value + 10
        time.sleep(0.1)
        print('sum-2',shared.value)
    lock.release()  # 整个for 循环结束后才释放锁

# 如果是一个数组为共享资源，那么 S = mp.array('i',[1,2,3])
S = mp.Value('i', 0) 

# 定义一个锁
lock = mp.Lock()

# 分别启动2个进程
process1 = mp.Process(target=worker, args=(S, 'Process-1',lock,))
process2 = mp.Process(target=job, args=(S, 'Process-2',lock,))

print('start...')
process1.start()
process2.start()
process1.join()
process2.join()
print('end...')

