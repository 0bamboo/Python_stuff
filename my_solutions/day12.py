# ================== Q44 =========================
print('============== Q44 ====================')
lst = list(map(lambda c: c ** 2, range(1, 21)))
print(lst)

# ==================== DONE ==========================
# ==================== Q45 ============================
print('===================== Q45 ===================')
class American:
    @staticmethod
    def printNationality():
        print('american')

hell = American()
hell.printNationality()

# =================== DONE ==========================
# =============== Q46 ===========================
print('==================== Q46 =================')
class American:
    pass
    class Newyorker:
        def new():
            print('im a newyorker')


American.Newyorker.new()

# ================================= THE END =================================