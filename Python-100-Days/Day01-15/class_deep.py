class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修饰器 setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋." % self._name)
        else:
            print("%s正在玩斗地主." % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 20
    person.play()
    # person.name = '李元芳'  AttributeError: can't set attribute


if __name__ == '__main__':
    main()
