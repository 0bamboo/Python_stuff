# =================== Q54 ======================
print('=============== Q54 =====================')
email = input('enter your email : ').split('@')
def handle_email(email):
    for i in range(len(email)):
        for char in email[i]:
            if char.lower() < 'a' or char.lower() > 'z':
                return ' wrong email address '
    return email[1]
import re
email[1] = re.sub('[.com]', '', email[1])
print(handle_email(email))

# ==============  DONE ================= 
# ======================= Q55================================
print('================= Q55 ====================')
words = input('write down some words : ').split()
digit = []
for item in words:
    for c in item:
        i = 1
        if c < '0' or c > '9':
            i = 0
            break
    if i:
        digit.append(str(item))

print(','.join(digit))

#  use isdigit() DUMBASS
# =================== DONE ====================
#  ==================== Q 56 =======================
print('========================= Q56 ===================')
print (u'hello , world')
# ======================= DONE ===================
# =============== Q57 ====================
print('=-======================= Q57 ================')
s = input('write down something : ')
u = s.encode('utf-8')
print(u)
# =================== DONE ====================
# ==================== Q58 =====================
print('================= Q58 ==================')
#  coding : utf-8
#  ======================  DONE =======================
# ========================== Q59 ======================
print('==================== Q 59 =====================')
num = int(input('enter a number : '))
sum = 0
for i in range(1, num+1):
    sum += i/(i + 1)
print('|{}|'.format(round(sum, 2)))

# ========================= THE END ==================