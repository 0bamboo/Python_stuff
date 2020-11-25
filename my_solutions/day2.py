# ====================== Q4 ==========================
print ('-------------- Q4 ----------------')

x = (input('> '))

def convert_to_t_l(ex):
    lis = ex.split(',')
    tup = tuple(lis)
    print(lis)
    print(tup)

convert_to_t_l(x)

# ===================== Q5 =============================
print ('----------------- Q5 -------------')

class ForStrings:
    def __init__(self, x):   #the constructor
        self.x = x

    def get_str(self):
        self.x = input('write down something > ')


    def print_str(self):
        print(self.x.upper())


string = ForStrings("hello")
string.print_str()
string.get_str()
string.print_str()

# =================== Q6 ==========================
print('---------------- Q6 ------------------')
import math
x = input('square method write nbr > ')
# y = x.split(',')
# q = math.sqrt((50*2*int(y[3]))//30)
# print(q)

def square_som(x):
    x = x.split(',')
    for i in x:
        print(int(math.sqrt((2*50*int(i))/30)), end = ',')


square_som(x)
print()

# =================== Q7 ===================
print ('------------ Q7 -------------')

dig_lis = input('2d > ')
dig_lis = dig_lis.split(',')
rows = int(dig_lis[1])
cols = int(dig_lis[0])
def convert_to_2d(x,y):
    lis = list()
    for i in range(x):       # columns
        col = list()
        for j in range(y):   # rows
            col.append(j * i)
        lis.append(col)
    print(lis)


convert_to_2d(cols, rows)
# ==== another method ======


# =============== Q8 =========================
print('------------- Q8 ------------')
given_lis = input('type > ').split(',')
print(given_lis) 
def sort_alpha(word):
    word.sort(reverse=True)
    for word in word:
        print(word, end = ',')


sort_alpha(given_lis)
print()

# another method easy one
lst = input('> ').split(',')
lst.sort()
print(','.join(lst))

#  U NEED TO LOOK FOR MAP FUNCTION AND LAMPDA FUNCTION AND JOIN
# ================ Q9 =========================
print('----------------- Q9 ---------------')
#  there is a bug here fix it!!!!
lis = []
while 1:
    line = input()
    if len(line) == 0:
        break
    lis.append(line.upper())
    
for line in lis:
    print(line)

