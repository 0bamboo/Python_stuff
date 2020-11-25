# ================================ Q16 =====================
print ('------------------- Q16 ---------------')
lis = input('enter numbers separate with , > ').split(',')
lis_odd = [pow(int(x), 2) for x in lis  if not int(x) % 2 == 0]
lis_odd = [str(x) for x in lis_odd]
print (','.join(lis_odd))

# =========================== Q17 ============================
print('---------------- Q17 ----------------')
lis_data = list()
lis_s = []
total = 0
while 1:
    st = input()
    if st == '':
        break
    lis_data.append(st)

for item in lis_data:
    for i in item:
        if i.upper() == 'D':
            lis_s.append(item.split())
            break
for item in lis_s:
    total += int(item[1])

print(total)    

# ======================== DONE ========================