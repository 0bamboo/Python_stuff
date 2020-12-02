# ==================== Q20 ======================
print('---------------- Q20 ---------------')

class Div_by_7:
    def div(self, n):
        for i in range(n + 1):
            if i % 7 == 0:
                print(i)
div = Div_by_7()
div.div(int(input('> ')))

# ================ Q21 ===================
import math

print('--------------- Q21 ----------------')
lis = []
x, y, dist = 0, 0, 0
while 1:
    steps = input().split()
    if not steps:
        break
    lis.append(steps)

for item in lis:
    print(item[0])
    if item[0].upper() == "UP":
        x += int(item[1])
    if item[0].upper() ==  'DOWN':
        x -= int(item[1])
    if item[0].upper() == "RIGHT":
        y += int(item[1])
    if item[0].upper() ==  'LEFT':
        y -= int(item[1])
print(x,y)
dist = math.sqrt(x ** 2 + y ** 2)
print(dist)

# ===================== DONE =================