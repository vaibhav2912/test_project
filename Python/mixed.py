
#===============================================================================
# # ********exec function********
#
# x = input("Enter the operation to be done") #enter print
# y = input("Enter the string to be printed") #Enter string to be printed
# cmd = f"{x}(\"{y}\")"
# exec(f"{x}(\"{y}\")")
#===============================================================================


#===============================================================================
# # ********enumerate function********
#
# a = ['spring','summer','fall','winter']
#  
# for i,j in enumerate(a, start = 1):             
#     print(i,j)
#===============================================================================


#===============================================================================
# # ********filter function********
#
# a = [1,2,3,4,5,6]
# b = [2,4,6,8,9]
# c = []
# 
# for i in a:
#     if len(list(filter(lambda x: x == i, b))) != 0:
#         c.append(i)
#         
# print("common elements in a and b are {}".format(c))
#===============================================================================


#===============================================================================
# # *******map function************
# 
# a = [1,2,3,4,5]
#  
# def square(x):
#     return(x * x)
#  
# def cube(x):
#     return (x * x * x)
#  
# functions = [square, cube]
#  
# for func in functions:
#     b = list(map(func, a))
#     print("{} of all the numbers in array is: {}".format(func, b))
#===============================================================================



#===============================================================================
# # ******Factorial of a number using reduce function*********
#  
# from functools import reduce
#   
# num = int(input("Enter the number to find factorial: "))
# result = reduce(lambda x,y: x*y, range(1, num + 1))
#   
# print( "Factorial of {} is: {}".format(num, result))
#===============================================================================


a = [20,21,1,2,2,3,4,5,5,6,7]
b = [1,2,2,3,4,5,5,6,7,10,12]
temp = dict(zip(a,b))
print(temp)
d = dict(this = "ye", dog = "kutta", cute = "sundar")
str1 = "this dog cute"
str2 = []

d.update(this = "ha", dog = 'kutra')

for i in str1.split(' '):
    if i in d.keys():
        str2.insert(str1.index(i), d[i])
str3 = ' '.join(str2)
print(str3)
#print(d.setdefault(temp))

print("d: ", d)
e = list(d.values())

print("e: ", e)
a = set(a)

b = set(b)

print("a.difference(b): ", a.difference(b))
print("b.difference(a): ", b.difference(a))
print("b is proper subset of a: ", b < a)
print("Symmetric difference: ", a.symmetric_difference(b))
print("Symmetric difference: ", a.difference(b).union(b.difference(a)))

print(a)

d = dict(this = "ye", dog = "kutta", cute = "sundar")

pairs = [(v, k) for (k, v) in d.items()]
pairs_dict = dict(pairs)
print(pairs)
print(pairs_dict)

# Collections

import collections


# deque

DQ = collections.deque ([1,2,3,4,5], 50)
print(DQ)
DQ.append(6)
DQ.appendleft(7)
print(DQ)
DQ.pop()
DQ.popleft()
print(DQ)
DQ.rotate(3)
DQ.extend(d.items())
print(DQ)
print(DQ[5])

# Unix tail like functionality using fixed size deque: 
# For Full deque, if elements are added at the front or back
# equivalent number of elements are removed from the opposite end of deque

def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return collections.deque(f, n)
    
for i in tail("../CourseTimes.txt", 2):
    print(i.rstrip('\n'))
    
# defaultdict

d_list = ['one', 'two', 'three', 'four', 'five']
d1_list = [1, 2, 3, 4, 5]
d1_dict = dict(zip(d_list, d1_list), six = 6, seven = [1,2,3])
d1_dict['one'] = []
d1_dict['one'].append(3)
d_dict = collections.defaultdict(list)

#for i in d_list:        #This loop and the next statement do the same exact thing
#    d_dict[i]
d_dict.update(zip(d_list, d1_list))   #This statement and the for loop above do the same exact thing

d_dict['one'] = "Vaibhav"
print(d_dict)
print(d1_dict)

# OrderedDict

ord_dict = collections.OrderedDict(zip(d_list, d1_list))
print(ord_dict)
print(ord_dict.popitem(last = False))
print(ord_dict)
ord_dict.move_to_end('five', last = False)
print(ord_dict)