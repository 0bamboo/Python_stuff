# string = 'hello world'
# print(string[4::])

# ====== FORMATED STRINGS ========
name = 'abdennacer'
last = 'ama'
# STRING CONCATENATION
message = name + ' [' + last + '] is a programmer'
# ===>> FORMATED STR
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
print('--------------- arithmetics operators --------------')
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
print ('prenthesis then exp first then mult then div .... '+ str(x))

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
    print(f'the price of the house now is = {price} $')
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
print('----------------weight converter----------')
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
#  range function ex :for item in range(3) 
#                           print (item)   = 0 
#                                            1 
#                                            2 
# ===========ex======
# augmented assignement operator += , //= , -=, *= ...
print('------------ex calcul total using for loop---------')
total = 0
prices =[199, 304, 39, 34, 99]
for item in prices:
    total += item
print(f'total : |{total}|')

# ======================= NESTED LOOPS==================
print('----------ex coordinates--------')

for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')
print('-----------CHALLENGE---------')

challenge = [2, 2, 2, 2, 7]
# using cheat method hahahah
# for item in challenge:
#     print('x' * item)
# using dumb method hahahah
# for i in challenge:
#     if i == 5:
#         print('xxxxx')
#     else:
#         print('xx')
# using nested loops
for i in challenge:
    out = ''
    for r in range(i):
        out += 'x'
    print(out)
# =========================== LISTS =============================
names = ['abdenncer', 'paayk', 'mugiwara', 'kumaa']
print(names)
print(names[:])
print(names[-2])
print(names[2:])
print(names[3:3])
print(names[1:-4])
names[-1] = 'kuma'
print(names[3])
# ===== find the largest number in the list =====
print('------find the largest numbed in the list-----')
find_largest = [43, 66643, 5, 4385, -33, 209, 23, 849, 32, 9889999, 23878723]
largest_nbr = 0
for i in find_largest:
    if i > largest_nbr:
        largest_nbr = i
print(f'largest number is : {largest_nbr}')
# =========================== 2D LISTS =================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    for j in i:
        print(j)
# =========== list methods ===============
numbers = [3, 5, 6, 7, 4, 3, 9]
numbers.append(13) #to add an item at the end of the list
numbers.insert(3, 10) #to add an item in list wherever you want (index, item_to_be_added)
numbers.clear() # to delete the list
# numbers.remove(9) # to remove an item on the list
for i in range(7, 26):
    numbers.append(i ** i % 3)
print(numbers) 
print(numbers.pop()) #to remove the last item on the list
print(numbers)
ind = numbers.index(2) # to check for an item on the list it returns the index of first occurance of the item
print(ind)
numbers.count(1) # to count the items of the list 
numbers.sort() # to sort the items 1234
numbers.reverse() # to reverse the list 
numbers.copy() # to get the copy of the list
# ============  ex to remove duplicates on the list ===========
print('-------------------- remove dups ---------------')
lis = [2, 3, 4, 5, 6, 4, 3, 2, 2, 2, 4]
another_lis = []
for item in lis:
    if item not in another_lis:
        another_lis.append(item)   # dont think to much ;)
print(another_lis)

# ======================= TUPLES==================
numbers = (1, 2, 5) #====> tuple you can not change its items unchangeable
# ====================== UNPACKING===============
num = (2, 3, 5)
x = num[0]
y = num[1]
z = num[2]
 # || this equal to :
x, y, z = num
# =============== DICTIONARIES =================
person = {
    "name": "abdenncer ama",
    "age": 22,
    "school": "1337 school"
}
print(person["name"])
print(person.get("school"))
# =================== exercie =============
# phone_nbr = input('phone number : ')
# numb = {
#     "1": ' one ',
#     "2": ' two ',
#     "3": ' three ',
#     "4": ' four ',
#     "5": ' five ',
#     "6": ' six ',
#     "7": ' seven ',
#     "8": ' eight ',
#     "9": ' nine ',
#     "0": ' zero '
# }
# ret_val = ""
# for i in phone_nbr:
#     ret_val += " " + numb.get(i, "error!")    
# print(ret_val)

# =================== Another exercice(emojis) =================
emo_lis = input('> ')
def ft_convert_to_emojis(lis, emo_lis):
    lis = emo_lis.split(' ') 
    emojis = {
        ':)':'😊',
        ':(':'☹',
        'sleepy':'😴',
        'upset':'😠',
        'sick' :'🤒😷🤧🥶'
    }
    emo_lis = ""
    for i in lis:
        emo_lis += emojis.get(i, i) + ' '
    return (emo_lis)
lis = ""
pr = ft_convert_to_emojis(lis, emo_lis)
print(pr)
# ========================= FUNCTION ====================
print('=============== FUNCTIONS ==============')
def ft_first_func(my_name, my_lastn):
    print(f'Hello {my_name} {my_lastn} from the first function')
total = 0.0
def calc_cost(items, shipping, discount ):
    return ((items * discount) + shipping)

print('first func will be executed : ')
ft_first_func("abdennacer", "ama")                          #===>>positional arguments     | positional args used before keyword args
ft_first_func(my_lastn = "ama", my_name = "abdennacer")     #===>>keyword arguments        |

total = calc_cost(items = 342, shipping = 43, discount = 0.5)
print(total)

# =================================== Handling errors (exceptions)======================
print('--------------------- exceptions (errors handling)--------------')
try:
    age = int(input('what is your edge : '))
    print(age)
    money = 2000 / age
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError: #instead of crashing the program we will print an error msg
    print ('Invalid error')

# ====================== CLASSES ======================================

print ('------------------ CLASSES -------------')

# defining a class 

class Point:
    def __init__(self, x, y): # the constructor fucntion 
        self.x = x
        self.y = y

    def move(self):
        print('the player start moving')

    def draw(self):
        print('the player start drawing ')
# create an object 
pointt = Point(10, 20)
pointt.draw()
# an object plus an attribute
# pointt.x = 34
print(pointt.x)

class Person:
    def __init__(self, name): 
        self.name = name

    def talk(self):
        print (f'talk amigo {self.name}')

namee = Person("abdennacer")
namee.talk()

# ===================== INHERITANCE ==============
class Som:
    def walk(self):
        print('start walking')

class Dog(Som):
    pass            #pass means nothing defined 

class Cat(Som):
    def __init__(self, name):
        self.name = name
    def jump(self):
        print(f'jump little {self.name} jump !!')

doggy = Dog()
cattie = Cat("lucy")
doggy.walk()
cattie.jump()


# ========================= MODULES ====================

import converters  # we import our module , we import everything in the module 
from converters import kg_to_pounds #we import only the funct kg_to_pounds

print (kg_to_pounds(77))
print (converters.kg_to_pounds(45))
print (converters.pounds_to_kg(145))

print('----------------------- exercice--------------')

from utils import find_max

tab = [45, 949, 00, 4, 3343, 33, 283, 3232, 9594, 403, 979, 333]
print(find_max(tab))

#PACKAGES fiels inside folders import those files like this :
# import folder.file or from folder import file

# ===========built in modules like math random ....
import random

print (random.random())
# choose the best player in history

players = ['messi', 'ronaldo', 'maradona', 'pele', 'cr7', 'kreuf']
best = random.choice(players)
print(best)

# ==============exercice==================
print('-----------ex roll a dice ------------')
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)

dice = Dice()
print(dice.roll())

# ======================= How To Work With Files And Directories =======================
from pathlib import Path


# absolute path "startion from the root "
# relative path "starting from the current directory"

py_path = Path("path_check")
r = py_path.exists()   #checks if the existence of the folder in current folder
print (r)

p_path = Path()
for file in p_path.glob('*.py'):   # method for searching for files or (directories) with ext py in the current folder
    print(file)
