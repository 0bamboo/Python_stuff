# ======================== Q22 =============================
print('================ Q22 ====================')
in_put = input('> ').split()
in_put.sort()
in_dict = {}
for item in in_put:
    in_dict[item] = str(in_put.count(item))
for item in in_dict:
    # print(item + ':' + in_dict[item])
    print('{0}:{1}'.format(item, in_dict[item]))


# ================== DONE ===========================
# ====================== Q 23 =========================
print('============= Q23 =======================')

number = int(input())
print(number**2)

# ================= DONE ======================
# =================== Q 24 =================================
print('================== Q24 ===================')

def does_nothing():
    ''' this function does nothing actually this it's just an example of docstring '''

help(does_nothing)
print(does_nothing.__doc__)
# ============== DONE ==================
# ===================== Q25 ==================================
print('======================= Q25 ======================')
class This_example:
    def __init__(self, var1):
        self.var1 = var1
    def return_var(self):
        return(self.var1)

#  ================= END =========================