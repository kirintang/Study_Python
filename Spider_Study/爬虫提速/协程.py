# 一般情况下，但程序处于IO操作的时候，线程都会处于阻塞状态

# 协程：但程序遇见IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的切换，切换操作一般就是IO操作
# 在宏观上，我们能看到的其实是很多个任务一起执行
# 多任务异步操作

# 上方都是在单线程条件下

import asyncio
import time


""" async def func():
    print("hello, my name is mantis")


if __name__ == '__main__':
    g = func()  # 异步协程的函数，得到的是一个协程对象
    asyncio.run(g)  # 协程程序需要asyncio模块支持 """


""" async def func1():
    print("hello, my name is tom")
    # time.sleep(3)  # 但程序出现同步操作的时候，异步就中断了
    await asyncio.sleep(3)
    print("hello, my name is wusong")


async def func2():
    print("hello, my name is wudalang")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("hello, my name is songjiang")


async def func3():
    print("hello, my name is jishiyu")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("hello, my name is luzhishen")

if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [f1, f2, f3]
    t1 = time.time()
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2 - t1)
 """


async def func1():
    print("你好，我叫潘金莲")
    await asyncio.sleep(3)
    print("你好，我叫武松")


async def func2():
    print("你好，我叫武大郎")
    await asyncio.sleep(2)
    print("你好，我叫松江")


async def func3():
    print("你好，我叫鲁智深")
    await asyncio.sleep(4)
    print("你好，我叫李逵")


async def main():
    """ # 第一种写法
    f1 = func1()
    await f1 # 一般await挂起操作放在协程对象里 """
    # 第二种写法
    # tasks = [func1(), func2(), func3()] # 3.8之前使用的方式
    # 3.8之后的版本使用下面的方式
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func2()),
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
