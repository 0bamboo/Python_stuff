# ===================== Q47 ============================
print('================= Q47 =======================')
import math
class Circle:
    def __init__(self, r):
        self.radius = r
    def calc_area(self):
        return math.pi * self.radius ** 2

r = int(input('enter a radius : '))
area = Circle(r)
print('the area of circle of radius equal to {} is : {} '.format(r, area.calc_area()))

# =========================== DONE ======================
#========================== Q48 ===================
print('================= Q48 ==================')
class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def calc_area(self):
        return self.w * self.h

w = int(input('width = '))
h = int(input('height = '))
rect_area = Rectangle(w, h)
print('the area of the rectangle is : {}'.format(rect_area.calc_area()))
# ==================== DONE ========================
# =================== Q49 ==========================
print('================= Q49 ======================')
import random
class Shape:
    def __init__(self):
        pass
    def calc_area(self):
        return 0 * random.random()
class Square:
    def __init__(self, length = 0):
        self.l = length
    def calc_area(self):
        return self.l * self.l
    
lin = int(input('enter a length : '))
sha = Square(lin)
print('the area of the square is : {}'.format(sha.calc_area()))
print('the area of the shape is : {}'.format(Shape().calc_area()))
# ======================== DONE ============================
# ========================= Q50 ===================
print('==================== Q50 ======================')
i = input('enter a digit : ')
if i < '0' or i > '9':
    raise RuntimeError('this character |{}| is not a digit'.format(i))
else:
    print(i)

# ============================= T H E  E N D =====================