# ============================ Q51 ============================
print('=================== Q51 ===================')
def calc_5_0():
    return 5 / 0

try:
    i = calc_5_0()
    print(i)
except ZeroDivisionError:
    print(' DUMB ASS YOU CAN NOT DEVIDE ANY NUMBER BY ZERO ')

# ======================= DONE ========================
# ===================== Q52 ========================
print('================== Q52 ======================')
class Error(Exception):
    def __init__(self, err):
        self.r = err

n = int(input('enter a number : '))
try:
    if n < 0:
        raise Error('the number is negative ')
    elif n > 100:
        raise Error('the number is too big ')
except Error as r:
    print('the error raised : ' + r.err)

# ==================== DONE =======================
# =================== Q53 =======================
print('================= Q53 =====================')
email = input('enter an email : ').split('@')
print(email[0])

# =========================== THE END =======================