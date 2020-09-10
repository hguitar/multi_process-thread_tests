from multiprocessing import Process, Queue, Value
from random import randint  # typo: Unused import
from time import time
import os
from typing import Any
result_queue = Queue()



def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


# check all process status
# alive = 1 dead = 0
# calculate all results
# is all is dead then return False
def is_processes_finished(process_list):
    list_len = len(process_list)
    status = 0
    while 1:
        # 检查所有process
        for p in process_list:
            # 如果process dead
            if not p.is_alive():
                # 状态加1
                status += 1
                # 将dead process移除
                process_list.remove(p)
                # 如果状态=list长度,表示所有process跑完
                # 返回false
                if status == list_len:
                    return False


def start_all_process(process_List):
    for p in process_List:
        p.start()


def consctruct_all_processes():
    processes = []
    number_list = [x for x in range(1, 100000001)]

    index = 0
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
    return processes


def main():

    processes = consctruct_all_processes()

    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    total += result_queue.get()
    print(total)
    end = time()
    print('time in sec: %.2f' % (end-start))


if __name__ == '__main__':
    main()