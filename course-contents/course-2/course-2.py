# Today's outline:

# 1. loops and iterations
# 2. modules
# 3. files
# 4. what is shell
# 5. class and objects
# 6. object oriented programming
# 7. inheritance

# 1. loops and iterations

# for loop

l = range(10)
a = 0
for number in l:
    a += number
    continue

# while loop
a = 5
while a > 0:
    a -= 1
    if a == 2:
        break
    continue

range(5) != list(range(5))  # O(1) vs O(n)

# 2. modules
import math  # put on the very top of the file
# from math import *
from math import factorial, gcd

# pip install numpy

# 3. files

# 1. python built-in approach
# 2. 3rd modules: numpy, pandas, opencv

f = open("C:/Users/VailG/codes/python-course/course-contents/course-1/note.md", 'r')
for line in f:
    # print(line)
    pass
f.close()

with open("C:/Users/VailG/codes/python-course/course-contents/course-1/note.md", 'r') as f:
    print(f.readline())

# 4. what is shell
