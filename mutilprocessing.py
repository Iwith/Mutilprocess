'''
1.创建多个进程,放到进程池里面
2.pool.join()运行进程池里面的进程
'''
#!/usr/bin/env python
import multiprocessing as mp
import time

def worker(num):
    for i in range(num):
        time.sleep(0.1)
        print(i)

# 进程池大小为5
p = mp.Pool(5)

# 将15个进程放到进程池里
for i in range(6):
    p.apply_async(worker,args=(10,))

p.close()  # close进程池之后就不能再往池里面加进程了
print('begin...')
p.join()   # 启动所有pool里面的进程，main进程等待所有的进程执行完毕才退出
print('end..')
