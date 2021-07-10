import hashlib
import random
import os
from io import BytesIO

from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

ALL_CHARS = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


def gen_random_code(length=4):
    return ''.join(random.choices(ALL_CHARS, k=length))


class Bezier:
    """贝塞尔曲线"""

    def __init__(self):
        self.tsequence = tuple([t/20.0 for t in range(21)])
        self.bezier = {}

    def make_bezier(self, n):
        """绘制贝塞尔曲线"""
        try:
            return self.beziers[n]
        except KeyError:
            combinations = pascal_row(n-1)
            result = []
            for t in self.tsequence:
                tpowers = (t ** i for i in range(n))
                upowers = ((1-t) ** i for i in range(n-1, -1, -1))
                coefs = [c*a*b for c, a,
                         b in zip(combinations, tpowers, upowers)]
                result.append(coefs)
            self.beziers[n] = result
            return result


class Captcha:
    """验证码"""

    def __init__(self, width, height, fonts=None, color=None):
        self._image = None
        self._fonts = fonts if fonts else \
            [os.path.join(os.path.dirname(__file__), 'fonts', font)
             for font in ['Arial.ttf', 'Georigia.ttf', 'Action.ttf']]
        self._color = color if color else random_color(
            0, 200, random.randint(220, 255))
        self._width, self._height = width, height

    @classmethod
    def instance(cls, width=200, height=75):
        """获取Captcha对象的方法"""
        prop_name = f'_instance_{width}_{height}'
        if not hasattr(cls, prop_name):
            setattr(cls, prop_name, cls(width, height))
        return getattr(cls, prop_name)

    def _background(self):
        """绘制背景"""
        Draw(self._image).rectangle(
            [(0, 0), self._image_size], fill=random_color(230, 255))

    def _smooth(self):
        """平滑图像"""
        return self._image.filter(ImageFilter.SMOOTH)


def random_color(start=0, end=255, opacity=255):
    """随机色值"""
    red = random.randint(start, end)
    green = random.randint(start, end)
    blue = random.randint(start, end)
    if opacity is None:
        return red, green, blue
    return red, green, blue, opacity
