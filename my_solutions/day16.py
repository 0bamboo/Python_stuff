# ================= Q 60 =======================
import math
print('=============== Q60 =====================')
def func_f(n):
    if n == 0:
        return 0
    else:
        return 100 + func_f(n - 1)

n = int(input('Enter a number : '))
nn = func_f(abs(n))
print('f({}) = {}'.format(n, nn))

# ===================== DONE =====================
# ====================== Q61 ===================
print('================= Q61 ================')
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input('Enter a number : '))
print('fibonacci({}) = {}'.format(num, fibonacci(abs(num))))
# ================= DONE ===============================
# ======================= Q 62 =====================
print('========================= Q62 ================')
lis = []
def fibona_lis(num):
    if num < 2:
        lis[num] = num
        return lis[num]
    lis[num] = fibona_lis(num - 1) + fibona_lis(num - 2)
    return lis[num]
num = int(input('Enter a number > 0 : '))
lis = [0] * (num + 1)
fibona_lis(num)
lis = [str(i) for i in lis]
print(','.join(lis))

# =================== DONE ======================
# ================== Q63 ======================
print('================= Q63 ===================')
def func_even(num):
    lis = []
    for i in range(num + 1):
        if i % 2 == 0:
            lis.append(str(i))
    print(','.join(lis))

num = int(input('type a number : '))
func_even(num)

# ====================  DONE ====================
# ========================== Q64 ====================
print('==================== Q64 ====================')
def generator_div(num):
    i = 0
    lis = []
    while i <= num:
        if i % 7 == 0 and i % 5 == 0:
            lis.append(str(i))
        i += 1
    print(','.join(lis))

num = int(input('type a positive number : '))
generator_div(num)

# ========================= THE END =======================