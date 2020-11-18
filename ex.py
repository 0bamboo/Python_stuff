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

print('-----------------ex------------')

# inp = input('inter your name : ')
# if len(inp) < 3:
#     print('the name must be at least 3 characters')
# elif len(inp) >= 20:
#     print('your name is too long its impossible to have a name like that are you stupid , aw i mean your father or mother whatever')
# else:
#     print(f'you have an amazing name {inp} ' * len(inp))

# =================PROJECT : WEIGHT CONVERTER==============

# w = int (input('Enter your weight : '))
# unit = input('kilos [ K ] or pounds [ P ] : ')
# if unit == 'k' or unit == 'K':
#     w = w * 2.21
#     print(f'your weight in Kg is : {w} p')
# elif unit == 'p' or unit == 'P':
#     w //= 2.21
#     print(f'your weight in pounds is : {w} kg')
# else:
#     print('the data is not correct !')

# ==========================WHILE LOOP=====================
i = 1
# while i <= 10:
#     print(f'[ {i} ]')
#     i += 1
# print('the loop is done')

while i <= 10:
    print('*' * i)
    i += 1
print('DONE')

# ================GUESS GAME =============
print('----------------------GUESS GAME-------------')
# i = 0
# while i < 3:
#     guess = int (input('Guess the number : '))
#     if guess == 1 or guess == 0:
#         print('You win !')
#         i = 3  # break 
#     i += 1
# if i == 3: #you can use else for while if the loop finished without break the code in this else block will be executed
#     print('You have only 3 trys good luck next time !')
# ===============GAME CAR===================
print('-------------------------GAME CAR -------------------')
# i = j = 0
# while 1:
#     the_given_str = input('>')
#     if the_given_str == "help":
#         print('''
#     start ---> to start the car
#     stop  ---> to stop the car 
#     quit  ---> to quit the game
#         ''')
#     elif the_given_str.lower() == "start":
#         if i == 0:
#             print('car started .... ready to go !')
#             i = 1
#         else:
#             print('Hey car already started .')
#     elif the_given_str.lower() == "stop":
#         if j == 0:
#             print('Hey car stoped .')
#             j = 1
#         else:
#             print('car already stoped .')
#     elif the_given_str.lower() == "quit":
#         print('game over')
#         break
#     else:
#         print('i do not understand . please check help command ')
# ========================= FOR LOOP===========================

# str = input('enter your passward : ')
# for i in str:
#     print(i)

# ===========ex======
# augmented assignement operator += , //= , -=, *= ...
total = 0
prices =[199, 304, 39, 34, 99]
for item in prices:
    total += item
print(f'total : |{total}|')