# =============================== Q85 ===============================
print('====================== Q85 ========================')
lis = input('Please enter a list of numbers :').split()
lis = [d for i,d in enumerate(lis) if i != 0 and i != 4 and i != 5] # not in (0,4,5)
print('The list after modifiying : ', lis)
# ================= DONE ================================
# ================== Q86 ===========================
print('========================== Q86 =======================')
lis = input('Please enter another list of nums :').split()
lis = [lis[i] for i in range(len(lis)) if int(lis[i]) != 24] # use the method lis.remove()
print('The list after removing the num 24 : ', lis)
# ==================== DONE ==================
# ====================== Q87 ====================
print('================== Q87 ============================')
lis1 = set(input('Please enter first list of nums :').split())
lis2 = set(input('Please enter second list of nums :').split())
print('The intersection between first list and second is :', set.intersection(lis1, lis2)) # or use lis1 & lis2 instead
# ===================== DONE ======================
# ======================== Q88 =============================
print('================== Q88 =====================')
lis = input('Please enter a list of numbers :').split()
lis = set(lis)
# lis = list(lis)
print('The list of numbers after removing duplicates :', lis)
# ====================== DONE =======================
# ============================= Q89 =========================
print('========================= Q89 =======================')
class Person:
    pass
class Male(Person):
    def getGender(self):
        print('MALE')
class Female(Person):
    def getGender(self):
        print("FEMALE")

child = Male()#Female()
child.getGender()

# ================================= THE END ===============================