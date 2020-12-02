#  ================== Q14 ===================
print('---------------- Q14 ---------------')
st = input('print a sentence > ')
up = 0
low = 0
for sen in st:
    if sen >= 'A' and sen <= 'Z':
        up += 1
    elif sen >= 'a' and sen <= 'z':
        low += 1

print(st)
print(f'UPPERCASE : {up} \nLOWERCASE : {low}')

# ================ Q15 ========================
print('----------- Q15 ----------------')

# fin ghadi fin awa ghadii hhhhhh
import random

st = input('write a+aa+...> ')
total = 9
a = 2
for i in st:
    if i == '+':
        total += 10 ** a - 1
        a += 1
print(total)

#  ==== the right solution ========
re = int(input('write a digit > '))
def ft_(a, b):
    st = ''
    for i in range(a):
        st += str(b)
    return st


a = 1
b = re
re = 0
while a <= 5:
    re += int(ft_(a, b)) 
    a += 1
    
print(re)



