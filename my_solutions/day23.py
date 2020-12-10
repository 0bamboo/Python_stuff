# ============================== Q97 ========================
print('======================== Q97 ==========================')
n = int(input('Enter a number : '))
alpha = "abcdefjhgklmnopqrstvwxyz"
index = n - 1
num_ = (n - 1) * 4
tmp = ""
tmp += '-' * (num_ // 2)
tmp += alpha[index]
tmp += '-' * (num_ // 2)

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