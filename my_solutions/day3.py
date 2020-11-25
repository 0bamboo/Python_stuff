# ======================= Q10 =========================
print('---------------- Q10 ---------------')
words = input('write down some words > ').split()
words.sort()
for word in words:
    if words.count(word) > 1:
        words.remove(word)

print (' '.join(words))

# ==================== Q11 =====================================
print ('------------- Q11 --------------------')
#  it is a fucking C waaaaay use python way  dumb ass hahahahahaha
binary = input('print a binary seperated with , > ').split(',')
in_bin = []
for b in binary:
    b = int(b)
    in_bin.append(b)
lis=[]
r = 0
for b in in_bin:
    i = 0
    decimal = 0
    j = 0
    r = b
    while b > 0:
        i = b % 10
        b //= 10
        decimal = decimal + i * pow(2,j) #2 ** j
        j += 1
    if decimal % 5 == 0:
        lis.append(str(r))
    
print(' '.join(lis))

# ======================= Q12 ================================
print('------------------- Q12 ----------------------')

# nbr = int(input('write down a bigger number than 999 > '))
#  C way again hahahahahahhah 
lis_nbr = []
nbr = 0
for i in range(1000,3000):
    d = 0
    j = 0
    nbr = i
    while i > 0:
        d = i % 10 
        i //= 10
        if d % 2 != 0:
            j = 1
            break
    if j == 0:
        lis_nbr.append(str(nbr))

print(' - '.join(lis_nbr))

# ===================== Q13 ==========================
print ('------------- Q13 ------------------')

st = input('print something > ')
letters, digits = 0,0
for i in st:
    if ord(i) < 48 or ord(i) > 57:
        letters += 1
    else:
        digits += 1
print(st)
print(f'LETTERS = {letters}')
print(f'DIGITS = {digits}')