# ========================= Q90 ==============================
print('========================== Q90 ==========================')
st = input('Enter a string :')
dic = {}
for i in st:
    dic[i] = st.count(i)
itm = dict(sorted(dic.items()))
for i in itm:
    print('{},{}'.format(i, itm[i]))
# =========================== DONE ==========================
# ======================== Q91 ================================
print('======================== Q91 ==========================')
st = input('Please enter a string : ')
print(st[::-1])

# ======================== DONE =======================
# ========================= Q92 =====================
print('==================== Q92 ===============================')
st = input('Please enter another str : ')
# print(''.join(c for c in st if not c.isdigit()))
pr = ''
for i in range(len(st)):
    if i % 2 == 0:
        pr += st[i]
print(pr)

# ============================= DONE ==========================
# ====================== Q93 ===================================
print('========================= Q93 ============================')
from itertools import permutations
lis = input('Enter a list of numbers : ').split()
lis = [int(d) for d in lis]
for perm in list(permutations(lis)):
    print(perm)

# =======================  DONE =============================
# ========================= Q94 ==============================
print('==================== Q94 ============================')
heads = int(input('Enter the number of heads : '))
legs = int(input('Enter the number of legs : '))
chickens = 0 # number of chickens
rabbits = 0 # number of rabbits
rabbits = int((legs - 2 * heads)/2)
chickens = heads - rabbits
if rabbits < 0 or chickens + rabbits != heads:
    print('SOME RABBITS OR CHICKENS HAS NO LEGS  HAHAHAH')
else:
    print('Number of chickens is : {} \nNumber of rabbits is : {}'.format(chickens, rabbits))
    
# =================================== DONE =================================