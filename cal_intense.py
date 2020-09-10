from time import time
from random import randint
from multiprocessing import Process, Queue


def task_handler(task_list, result_queue):
    """
    :type task_list: list
    :type result_queue: Queue
    """
    total = 0
    for num in task_list:
        total += num
    result_queue.put(total)


def main():


    start = time()


    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()
