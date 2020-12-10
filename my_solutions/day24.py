# ================================ Q100 =================================
print('============================== Q100 ============================')
lis = input('Enter a list of strings : ').split()
dic = {}
for item in lis:
    dic[item] = lis.count(item)
output= [dic[item] for item in dic]
print('The output is : ')
for item in output:
    print(item, end = ' ')
print()

# ========================= DONE ========================
# ========================== Q101 ==============================
print('========================= Q101 =========================')
lis = []
st = input('Enter a string : ')
for char in st:
    lis.append(char)
dic = {}
for item in lis:
    dic[item] = lis.count(item)
sorted_dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
for item in sorted_dic:
    print(item[0], item[1], end = ' ')
print()

# =============================== DONE ============================
# ========================= Q102 ====================================
print('======================== Q102 ===========================')
st = input('Enter a string : ')
num_dig = 0
num_alpha = 0
for char in st:
    if char.isdigit():
        num_dig += 1
    if char.isalpha():
        num_alpha += 1
print('Digit - {}'.format(num_dig))
print('Letter - {}'.format(num_alpha))

# ================================ DONE =========================
# ========================== Q103 =============================
print('========================= Q103 ===========================')
def recc(num):
    if num < 1:
        return 0
    return num + recc(num - 1)
num = int(input('Enter a number positive : '))
print('The sum of 1 to the number you entered is : {}'.format(recc(num)))



# =========================================================  T H E   E N D  =================================================