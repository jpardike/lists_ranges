# --------------------- LISTS & RANGES

# Lists are mutable (changeable)
# Lists can contain similar types of data

fruits = ['apple', 'banana', 'pear', 'grapes']

# Get Length
# fruits.length
# print(len(fruits))


# Accessing Elements
first_fruit = fruits[0]
last_fruit = fruits[-2]


# Adding Elements
fruits.insert(len(fruits), 'peach')
fruits.append('coconut')
fruits.extend(['nectarine', 'orange'])


# Change Values
# fruits[0] = 'apple'


# Deleting Values
# del fruits[0] # removes index position, does not return a value

# fruits.pop(1) # pop will take an optional index

# fruits.remove('peach') # remove wil remove the first element that matches the argument passed

# fruits.clear()

# print(fruits)



# ----------------- ITERATION

# for fruit in fruits:
#     print(fruit)

# for i, fruit in enumerate(fruits):
#     print(f"{i} - fruit")




# -------------- COMPREHENSIONS

nums = [1, 2, 3, 4, 5]
doubled_nums = []

for num in nums:
    doubled_nums.append(num * 2)


# Doubled Nums Comprehension
doubled_nums_comp = [num *2 for num in nums]



even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)


# Even Nums Comprehension
even_nums_comp = [num for num in nums if num % 2 ==0]


# print(even_nums_comp)


words = ['what', 'hump']

uppercase_words_comp = [word.upper() for word in words]

# print(uppercase_words_comp)


# -------------------- TUPLES

# Tuples are immutable (cannot change values)

colors = ('red', 'blue', 'purple')

colors2 = 'green', 'orange', 'yellow'

colors3 = 'polka-dot', # use a hanging comma to create a single item tuple

# blue = colors[1] # unpacking values

red, blue, purple = colors

# colors[1] = 'Blue' # Tuples do not support assignment or reassignment

# The len() method also works on tuples
# print(type(colors3))


# -------------- Iterating on Tuples

# for color in colors:
#     print(color)


# print(colors.index('blue'))



# ----------------------- RANGES

# Range returns a list of integers from start val to stop val, non-inclusive of stop val

# for number in range(11, 0, -1):
#     print(number)


# const people = 'john'
# const people2 = people

# people = ['kevin']

# Memory 
# | people | 00x234 | 00x234 |
# | people2 | 00x234 | 00x234 |

# HEAP
# | people | 00x234 | 00x234 |

# const people2 = people

# ------------------------ SLICES

# Slice takes start and stop vals (non-inclusive)
name = 'Alexandria'
copy = name[:]
nickname = name[0:4]

name = 'bob'

first_two_colors = colors[0:2]
last_two_colors = colors[1:3]

# copy/clone
colors_copy = colors[:]

print(colors_copy)