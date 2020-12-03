# ================== Q31 ==========================
print('================ Q31 ======================')

dic_of_nothing = {}
def print_dic(dic_of_nothing):
    for key in range(1, 21):
        dic_of_nothing[key] = key **2
        print('{0}:{1}'.format(key, dic_of_nothing[key]))

#  OR 
#  dict = {i: i**2 for i in range(1, 21)}

print_dic(dic_of_nothing)
# ================ DONE ==========================

# =================== Q32 ===========================
print('================= Q32  =======================')
def func_1(dict):
    dict = {i: i ** 2 for i in range(1, 21)}
    for i in dict:
        print(i, end = ' - ')
# OR  print(dict.keys())
dict = {}
func_1(dict)
# ====================== DONE ====================

#  ================== Q33 ========================
print('================ Q33 =========================')
def sqr_lis(sq_lis):
    sq_lis = [ i ** 2 for i in range(1, 21)]
    print(sq_lis)

sq_lis = []
sqr_lis(sq_lis)
# ==================== DONE ======================

# =============== Q 34 ========================
print('=================== Q34 =================')
def pr_first_five(sq_lis):
    sq_lis = [i ** 2 for i in range(1, 21)]
    # print(sq_lis[:5])
    for i in range(5):
        print(sq_lis[i])

sq_lis = []
pr_first_five(sq_lis)

#  ==================  DONE =====================

# ================== Q35 =======================
print('=============== Q35 =====================')
def pr_last_five(sq_lis):
    sq_lis = [i ** 2 for i in range(1, 21)]
    sq_lis.reverse()
    for i in range(5):
        print(sq_lis[i])

sq_lis = []
pr_last_five(sq_lis)

#  ========================= DONE =====================
#  ================== Q36 =====================
print('============== Q36 =======================')
def pr_except_first5(sq_lis):
    sq_lis = [i ** 2 for i in range(1, 21)]
    for i in range(5, 20):
        print(sq_lis[i])

sq_lis = []
pr_except_first5(sq_lis)

# ======================= DONE =======================

# ===================== Q37 ===================
print('================ Q37 ========================')

def pr_tuple(l):
    l = [i ** 2 for i in range(1, 21)]
    print(tuple(l))
    # for i in range(20):
        


l = []
pr_tuple(l)

#  ==================== END ===========================