class Student:
    # 初始化，类似构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s." % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("青少年模式")
        else:
            print("普通模式")


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    stu1 = Student('Jack', 19)
    stu1.study('Go语言编程之旅')
    stu1.watch_movie()

    test = Test('hello')
    test.__bar()
    print(test.__foo)


if __name__ == '__main__':
    main()
