#===============================================================================
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#         
#     print(student_marks)
#===============================================================================

#print (''.join([i.lower() if i.isupper() else i.upper() for i in input()]))

#===============================================================================
#input string swap case
#
# stringin = input()
# for i in stringin:
#     print(i.lower() if i.isupper() else i.upper(),end = '')
#===============================================================================
    
#===============================================================================
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
#     
# def split_and_join(line):
# return('-'.join(list(line.split(' '))))
#===============================================================================

#===============================================================================
#substitute a character in a string (string is immutable)
# string = "Vaibhav"
# 
# string = string[:5] + "k" + string[6:]
# print (string)
#===============================================================================

#===============================================================================
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# 
# NOTE: String letters are case-sensitive.
# 
# def count_substring(string, sub_string):
#     counter = 0
#     sub_len = len(sub_string)
#     for i in range(0, len(string)):
#         if string[i] == sub_string[0]:
#             if string[i:(i + sub_len)] == sub_string:
#                 counter = counter + 1
#     return counter
# 
# Sample Input
# 
# ABCDCDC
# CDC
# Sample Output
# 
# 2
#===============================================================================