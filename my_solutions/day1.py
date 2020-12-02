# ========= Q1 =======================

print('----------------- Q1 ----------------')
def func_find(): 
    # lis = []                            # to initialize a list we use these func list() or [] ....
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end = ', ')          # we use end to specifiy the end char for print func  the default is new line \n

func_find()
print(end = '\n')

# anotoher method using generators and list comprehension

# print(*(i for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0), sep = ',')

# ======== Q2 ============================
print ('----------------- Q2 ---------------')
def facto(self):
    fact = 1
    for i in range(1, self + 1):
        fact *= i
    return fact


# nbr = int (input('> '))
print(facto( int (input('> '))) , end = ',')

# another method using lambda function or  recursive funct

# def shortf(x):
#     return(1 if x <= 0 else x * shortf(x - 1))
print()
# =========== Q3 ========================
print ('--------------- Q3 --------------')

def dict_funct(x):
    d = {}           # or we use the this funct for initializing the dictionary dict()
    for i in range(1, x+1):
        d[i] = i * i
    return d
x = int (input('enter a number for dict > '))
print(dict_funct(x))

# ========== another method : using the dictionay comprehension

n = int (input('> '))
d = {i : i * i for i in range(1, n+1)}
print(d)

# ============== END OF THE DAY 1 ============================