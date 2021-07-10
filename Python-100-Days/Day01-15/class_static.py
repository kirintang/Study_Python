from math import sqrt


class Triangle:
    def __init__(self, l, w, h):
        self._l = l
        self._w = w
        self._h = h

    # 使用静态方法验证参数
    @staticmethod
    def is_valid(l, w, h):
        return l + w > h and w + h > l and l + h > w

    # 周长
    def perimeter(self):
        return self._l + self._w + self._h
    # 面积

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._l) * (half - self._w) * (half - self._h))


def main():
    l, w, h = 3, 4, 5
    if Triangle.is_valid(l, w, h):
        t = Triangle(l, w, h)
        print(t.perimeter())
        print(t.area())
    else:
        print("invalid")


if __name__ == '__main__':
    main()
