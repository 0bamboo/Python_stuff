# string = 'hello world'
# print(string[4::])

# ====== FORMATED STRINGS ========
name = 'abdennacer'
last = 'ama'
# STRING CONCATENATION
message = name + ' [' + last + '] is a programmer'
# ===>> FORMATED STRA
msg = f'{name} [{last}] is a programmer '
print('--------------- concatenation strs --------------')
print (message)
print('--------------- formated strs --------------')
print (msg)

#  ======= STRINGS METHODS ============
# func like strlen in c
print('--------------- len func --------------')
print(len(msg))
#  func uppercase
print('--------------- upper and lower funcs --------------')
print(msg.upper())
# func lower case
low = msg.lower()
print (low)
# func to search for a letters and words
search = msg.find('n')
print('--------------- find funcs --------------')
print(search)
# func to replace strs
rep = 'abdenncer ama is a lazy boy'
print('--------------- replace funcs --------------')
print(rep.replace('abdenncer','paayk_'))
#  check the existence or the sequence of a string
print('--------------- check existence --------------')
print('ama' in rep)
print('paayk_'in rep)

#  ============ ARITHMETIC OPERATIONS ===========
print('--------------- arithmetix operators --------------')
# float div 
print(10 / 3)
# int div
print(10 // 3)
# power
print (10 ** 2)
# modulo
print(19 % 7)
 
# ========== OPERATOR PRECEDENCE ===============
print('--------------- operator precedence --------------')
x = 10 + 4 * 3 ** 2
print ('prethesis then exp first then mult then div .... '+ str(x))

#  ============= MATH FUNCTIONS ===================
print('---------------Math funcs--------------')
import math
x = -3.6
y = 3.6
print(round(x))
print(abs(x))
print (math.ceil(x))
print (math.ceil(y))
print(math.floor(x))
print(math.floor(y))

#  ================ IF STATEMENT ==================
print ('--------- if statement -------------')
is_hot = True
if is_hot:
    print('drink planty of water')
print('enjoy your day :) ')
is_hot = False
if is_hot:
    print('go for swiming')
elif is_hot == True:
    print('its cold here')
else:
    print('just enjoy your day')
print("u did not go to the pool did you ?")
print('-----------------------EXO-------------------')
price = 1000000
good_cr = True
if good_cr:
    price = (1000000 * 10) / 100
    print('the price of the house now is = ' + str(price) + '$')
else:
    price = (1000000 * 20) / 100
    print('the price of the house now is = ' + str(price) + '$')

# =======================LOGICAL OPERATORS ==========================
print('-----------------logical operators------------')
has_high_income = True
has_good_credit = False
has_criminal_record = False
# if has_high_income and has_good_credit:
#     print('elegible for loan')
# else:
#     print('not elegible for loan')
if has_high_income or has_good_credit:
    print('elegible for loan')
else:
    print('not elegible for loan')
if has_high_income and not has_criminal_record:
    print('he is good for loan')

print('---------temp exo-------------')
temperature = 23
if temperature >= 30:
    print('let is go to swim')
elif temperature == 10:
    print('let is go to sky')
else:
    print('stay home and play video games :D ')
