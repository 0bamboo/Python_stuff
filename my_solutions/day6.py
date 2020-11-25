# =============================== Q18 =================================
print('-------------------- Q18 ------------------')

password = input('> ').split(',')
pr_pass = list()
for item in password:
    digi= 0
    low = 0
    up = 0
    rare = 0
    for c in item:
        if (c >= '0' and c <= '9'):
            digi = 1
        if (c >= 'A' and c <= 'Z'):
            up = 1
        if (c >= 'a' and c <= 'z'):
            low = 1
        if (c == '@' or c == '$' or c == '#'):
            rare = 1
    if (len(item) >= 6 and len(item) <= 12) and rare == 1 and up == 1 and low == 1 and digi == 1:
        pr_pass.append(item)

print(','.join(pr_pass))
# seriously C way again !!
# ==================== Q19 =========================
print('------------- Q19 -------------------')
lst = list()
while 1:
    tup = input(' ').split(',')
    if not tup[0]:
        break
    lst.append(tuple(tup))

lst.sort()
print(*lst, sep=", ")

# =================  DONE ======================