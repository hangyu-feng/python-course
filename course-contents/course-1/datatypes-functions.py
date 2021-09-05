print("Hello world!")
print("hi")

a = 5
b = 6
c = 7

# datatypes

# int
a = 3
a = 2 + 3 * 5**2
b = 11 // 2  # 5
c = 11 % 2  # 1
d = int(5.4)  # 5  <==> 5.4 // 1
print(a, b, c, d)

# float => double precision
a = 3.5
b = 7 / 2
c = 8 / 2  # 4.0
d = float(5)  # 5.0
print(a, b, c, d)

# str <-- string
# strings are immutable
a = "hello"
b = a + " world"  # b == "hello world"
print(a)
print(b)

# list
# lists are mutable
a = [1, 2, 3, 4, 5]
# list indexing
print(a[0])  # 1
print(a[4])  # 5
print(a[-1]) # 5
# list assignment
a[0] = 6
print(a)  # [6, 2, 3, 4, 5]
# list slicing ---- [)
a[0:3] == [a[0], a[1], a[2]]

b = [1, 'hello']

# tuple -- immutable list
a = (1, 2, 3)
# a[0] = 5  # can't do that!

a, b = 1, 2
a, b = b, a
print(a, b)  # 2, 1

# bool -- boolean
a, b = True, False
c = a == b  # c is False
a is True  # True
# boolean is a subclass of integer
# True == 1
# False == 0


# equivalence comparison
# ==  -> same value
# is  -> exactly same object

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

a = True
print(a is True)

if a:
    print("what is a?")

# logical operations
True and False  # true && false
True or False  # true || false
(not True) and True  # False

# range
range(5)
list(range(5))  # [0,1,2,3,4]  # list(range(0, 5, 1))
list(range(3, 9))  # [3,4,5,6,7,8]
list(range(1, 6, 2))  # 1, 3, 5
list(range(5, 0, -1))  # 5, 4, 3, 2, 1

# dict
a = {1: 3, 2: 4}  # {key: value}
a[1] == 3
a[2] == 4

b = [1, 2]

1 in a  # O(1)
1 in b  # O(n)  n = length of b
# hash function
a[3] = 5 # {1: 3, 2: 4, 3: 5}

# set
a = {1, 2, 3}
b = {3, 2, 1}
a == b
c = {3, 4, 5}
d = a | c  # {1,2,3,4,5}
d = a & c  # {3}
d.add(2)  # {2,3}


# functions
def f(a, b, c=3):
    return a + b + c

print(f(1, 2))  # 6
print(f(1,2,4))
print(f(a=1,b=2,c=4))
print(f(1,2,c=4))
print(f(b=1,a=2,c=4))


# list comprehension -> set, dict, tuple
a = [i*3 for i in range(5)]  # [0, 3, 6, 9, 12]

# same output
b = []
for i in range(5):
    b.append(i*3)

# loop
# for
for i in range(5):
    print(i)
# while
i = 0
while i < 5:
    print(i)
    i += 1
