# ================= Q 65 ================
print('============= Q 65 ==============')
lis = input('enter a list of numbers : ').split()
for i in lis:
    assert int(i) % 2 == 0, "list has an odd number"
print(lis)
# ================ DONE =================
# ================ Q66 ============================
print('===================== Q66 ================')
expression = input('Write an expression : ')
print(eval(expression))
# =========== DONE ================
# =================== Q67 ==================
print('=============== Q67 ======================')
def search(num):
    m_x = 0
    m_n = 0