# ============================== Q80 ==========================
print('========================= Q80 ========================')
lis = input('Enter numbers : ').split()
lis = [int(i) for i in lis if int(i) % 2 != 0]
print('The list after removing even numbers :', lis)
# ====================== DONE ==========================
#============================ Q81 =========================
print('====================== Q81 =========================')
ano = input('Enter another list of numbers : ').split()
ano = list(filter(lambda x: int(x) % 35 != 0, ano))
print('The list after removing numbers which are divisible by 5 and 7 :',ano)
# ===================== DONE ============================
# ======================= Q82 ==============================
print('=========================== Q82 ========================')
lis = input('Please enter another list of numbers ,Ya I now im a pain in ass : ').split()
lis = [d for i, d in enumerate(lis) if i % 2 != 0]
print('The list after removing the 0th and 2nd, 4th, 6th..... elements :', lis)
# ====================== DONE =======================
# ======================== Q83 ===========================
print('===================== Q83 ========================')
lis = input('Please enter another one , u know what i mean : ').split()
lis = [d for i, d in enumerate(lis) if i != 2 and i != 4]
print('The list after removing the 2nd and 4th element :', lis)
# ===================== DONE ======================
# ==================== Q84 =========================
print('==================== Q84 ====================')
lis =[[[0 for i in range(8)] for row in range(5)] for z in range(3)]
for i in range(3):
    print(lis[i])

# ================================= THE END ===============================