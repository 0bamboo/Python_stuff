# ============================== Q97 ========================
import sys
print('======================== Q97 ==========================')
n = int(input('Enter a number : '))
if n > 24 or n < 1:
    print('YOU NEED TO ENTER A NUMBER BETWEEN 1=< N =< 24 ')
    sys.exit()

ret_lis = []
ret_str = ''
alpha = "abcdefjhgklmnopqrstvwxyz"
index = n - 1
num_hphn = (n - 1) * 4 + 1
lis = []
i = 1
while i <= n:
    lis.append('-' * num_hphn)
    i += 1
sign = 1
for i, d in enumerate(lis[0]):
    if i % 2 == 0:
        ret_str += alpha[index]
        index -= sign
        if index == -1:
            sign = -1
            index += 2
        continue
    ret_str += d
ret_lis.append(ret_str)
ret_str = ''
anoth = ''
mult__ = 2
cnt = 0
while cnt < n - 1:
    var = len(ret_lis[0]) // 2 + 2
    ret_str = ret_lis[cnt][var:]
    anoth = ret_str
    ret_str = '-' * mult__ + ret_str[::-1]
    ret_str += anoth[1:] 
    ret_str += '-' * mult__
    print(ret_str)
    ret_lis.append(ret_str)
    cnt += 1
    mult__ += 2
# ret_str += ret_lis[0][var:]
# anoth += ret_lis[0][var:]
# ret_str = ret_str[::-1]
# ret_str += anoth[1:]
# print(ret_str)

print(alpha[index])
print(ret_lis)
print(lis)

#  the method that im going to use is like this :
# first im gonna fill all the blocks with hyphens then .... see you tomorrow









































# # =================== DONE ==================================
# # ======================== Q98 ===========================
# print('====================== Q98 =========================')
# import calendar as cl
# lis = input('Enter the date : ').split()
# lis_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# day = cl.weekday(int(lis[-1]), int(lis[1]), int(lis[0]))
# print(day)
# print('The day is : {}'.format(lis_days[day]))

# # =========================== DONE =========================
# # ============================= Q99 ===========================
# print('========================= Q99 ==========================')
# first_set = list(map(int, input('First set : ').split()))
# second_set = list(map(int, input('Second set : ').split()))
# output = []
# for item in first_set:
#     if item not in second_set:
#         output.append(item)
# for item in second_set:
#     if item not in first_set:
#         output.append(item)
# output.sort()
# # print('The symmetric difference is : {}'.format(output))
# for item in output:
#     print(item , end = ' ')
# # =================================  THE END =================================