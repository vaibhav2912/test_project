#===============================================================================
# n = int(input())
# arr = list(map(int, input().split(' ')))
#   
# high = max(arr)
# mid = arr[0]
#     
# for i in arr:
#     if i < high and i > mid:
#         mid = i
#             
# print(f"the second largest element in the input is {mid}")
# 
# #===============================================================================
# # Sample Input
# #  
# # 5
# # 2 3 6 6 5
# #===============================================================================
#===============================================================================


#===============================================================================
# #Kaushik Twitter
#
# cmdinput = input("$")
# cmdsplit = cmdinput.split(' ')
# 
# if (cmdsplit[0] != "validate_approvals"):
#     print("invalid command: {}".format(cmdsplit[0]))
# else:
#     print(cmdsplit)
# 
# for i, sub in enumerate(cmdsplit):
#     if(sub.startswith("--")):
#         if(sub == "--approvers"):
#             print(sub)
#             print(cmdsplit[i + 1: i + 3])
#===============================================================================



#===============================================================================
# #print format
#
# import sys
# 
# i , j , k = 1, 2, 3
# print(i,j,k,sep = '\n', end = '\n', file=sys.stdout)
#===============================================================================



#===============================================================================
# # list comprehension
# n = 2
# x, y, z = 1,1,1
# 
# print([[i,j,k] for i in range(0,(x+1)) for j in range(0,(y+1)) for k in range(0,(z+1)) if (i+j+k) != n])
#===============================================================================



#===============================================================================
# #Find Second Largest Number
# 
# l = [2,3,6,6,5]
# 
# max = max(l)
# l.sort()
# print(l[l.index(max) - 1])
#===============================================================================



#===============================================================================
# if __name__ == '__main__':
#     marksheet = []
#     for _ in range(0,int(input())):
#         marksheet.append([input(), float(input())])
# 
#     second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
#     print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
#===============================================================================



#===============================================================================
# # Swap case
# #===============================================================================
# # s = "VaibhAV PalanDE 1234"
# #
# # a = ""
# # for i in s:
# #     if(i.isupper()):
# #         a += i.lower()
# #     else:
# #          a += i.upper()
# # 
# # print(s)        
# # print(a)
# #===============================================================================
# 
# #===============================================================================
# # s = "VaibhAV PalanDE 1234"
# # a = ''.join(i.lower() if i.isupper() else i.upper() for i in s)
# # print(a)
# #===============================================================================
#===============================================================================


#===============================================================================
# # Change string content, add or remove content
# 
# a = "Vaibhav"
# b = "Palande"
# a = f"Hello {a} {b}! You just delved into python."
# print("Original string: ",a,sep = '\n', end = "\n\n")
# 
# print("Adding How are you? using slice: ")
# a = a[:23] + "How are you? " + a[23:]
# print(a)
# 
# print("\nAdding How do you do? using list: ")
# a = list(a)
# a.insert(36, "How do you do? ")
# a = ''.join(a)
# print(a)
#===============================================================================


#===============================================================================
# #===============================================================================
# # s = input()
# #     
# # count = 0
# #     
# # for c in s:
# #     if(c.isalnum()):
# #         count += 1
# #         break        
# # print("True") if(count > 0) else print("False")
# # count = 0
# # 
# # for c in s:
# #     if(c.isalpha()):
# #         count += 1
# #         break            
# # print("True") if(count > 0) else print("False")
# # count = 0
# #     
# # for c in s:
# #     if(c.isdigit()):
# #         count += 1
# #         break           
# # print("True") if(count > 0) else print("False")
# # count = 0
# #     
# # for c in s:
# #     if(c.islower()):
# #         count += 1
# #         break            
# # print("True") if(count > 0) else print("False")
# # count = 0
# #     
# # for c in s:
# #     if(c.isupper()):
# #         count += 1
# #         break            
# # print("True") if(count > 0) else print("False")
# # count = 0
# #===============================================================================
# #===============================================================================
# # S = input()
# # print (True if any(k in "0123456789" or k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False)
# # print (True if any(k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False)
# # print (True if any(k in "0123456789" for k in S) else False)
# # print (True if any(k in "abcdefghijklmnopqrstuvwxyz" for k in S) else False)
# # print (True if any(k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for k in S) else False)
# #===============================================================================
#===============================================================================


#===============================================================================
# # print octal number system
#   
# suffix, postfix = -1, 0
#   
# for i in range(50):
#     if((i % 8) == 0):
#         suffix += 1
#         print("|")
#     if i <= 7:
#         print(i, end = ' ')
#     else:
#         print("{}{}".format(suffix,postfix), end = ' ')
#         postfix += 1
#         if (postfix > 7):
#             postfix = 0
#===============================================================================


#===============================================================================
# # print octal, hex, binary
# 
# print("\nOctal: ")
# for i in range(50):
#     print("({}:{:o})".format(i, i), end = ' ')
# 
# print("\nBinary: ")
# for i in range(50):
#     print("(", i,":",format(i, 'b'),")", sep = '', end = ' ')
#     
# print("\nHex: ")
# for i in range(50):
#     print("(", i,":",format(i, 'X'),")", sep = '', end = ' ')
# 
# print("\n")
# octal = f"{format(i,'o')}".rjust(len(format(i, 'b')),'-')
# 
# print(octal)
#===============================================================================


#===============================================================================
# string = "hello    world   lol"
# string = string.split(' ')
# for n, i in enumerate(string):
#     if i.isalnum():
#         string[n] = i[0].upper() + i[1:]
# print(' '.join(string))
#===============================================================================



#===============================================================================
#  # Validating email addresses with filter()
#  
#  #==============================================================================
#  # input: 
#  # 3
#  # lara@hackerrank.com
#  # brian-23@hackerrank.com
#  # britts_54@hackerrank.com
#  #==============================================================================
#  
#  #==============================================================================
#  # Instructions:
#  # Valid email addresses must follow these rules:
#  # 1. It must have the username@websitename.extension format type.
#  # 2. The username can only contain letters, digits, dashes and underscores.
#  # 3. The website name can only have letters and digits.
#  # 4. The maximum length of the extension is 3. 
#  #==============================================================================
# 
# 
# def fun(email):
#     # return True if s is a valid email, else return False
#     splitat = email.split('@')
#     splitdot = email.split('.')
#     if(len(splitat) == 2 and len(splitdot) == 2):
#         username = splitat[0]
#         website, extension = splitat[1].split('.')
#         #print("username: ",username,"\n","website: ",website,"\n","extension: ",extension, sep='')
#         if ((website.isalpha() or website.isdigit() or website.isalnum()) and (len(extension) <= 3) and (username.isalpha() or username.isdigit() or username.isalnum() or '-' in username or '_' in username)):
#             return True
#         else:
#             return False
#     else:
#         return False
#     
# def filter_mail(emails):
#     return list(filter(fun, emails))
# 
# if __name__ == '__main__':
#     n = int(input("Enter number of entries: "))
#     emails = []
#     for _ in range(n):
#         emails.append(input("Enter email address: "))
# 
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print("Valid email addresses are: ")
# [print(i) for i in filtered_emails]
#===============================================================================

#===============================================================================
# import textwrap
#    
# ownerfilepathf = []
# with open("../CourseTimes.txt","r") as f:
#     for line in f:
#         #ownerfilepathf.append(line)
#         if (line.isspace() == False):
#             ownerfilepathf.append(textwrap.dedent(line).strip())
#            
# print(ownerfilepathf)
#===============================================================================

d = list()

def changeList(lst,*args,maxlength = 2):
    for i in range(maxlength):
        lst.append(args[i])

appendList = changeList
changeList(d,1,2,3,4,5,6,7,8,maxlength = 6)
print(d)