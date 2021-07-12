# 多线程
from threading import Thread  # 线程类


def func():
    for i in range(1000):
        print('func', i)


if __name__ == '__main__':
    t = Thread(target=func, args="t1")  # 创建线程并给线程安排任务
    t.start()  # 开始执行该线程，多线程状态为可以开始工作状态，具体执行的时间由cpu决定
    t2 = Thread(target=func, args="t2")
    t2.start()
    for i in range(1000):
        print('main', i)


# 也可以继承Thread类，重写run方法
""" class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print('子线程', i)


if __name__ == '__main__':
    t = MyThread()
    t.start() """
