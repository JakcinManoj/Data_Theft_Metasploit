#Sum in Single Line
# a = list(map(int,input().split()))
# print (a)
# print (type(a))
# print (sum(a))

#Count occurrence of letter in string
# a=str(input("Enter String: "))
# print("Enter letter to be count : ")
# x=input()
# b=a.count(x)
# print (b)

#Reverse String
#def fu(x):
#    return x[::-1]
# a=str(input())
# print (a[::-1])

#Maixmum no in list
# a=list(map(int,input().split()))
# print (a)
# print (max(a))

#For loop Program
# a=list(map(int,input().split()))
# n=len(a)
# for num in range(n):
#    print ('hello',num+1,(num+1)*".")


# a=list(map(int,input().split()))
# n=len(a)
# for num in range(0,n,2):
#    num=num+1
#    print(num)


#def ps(s):
#    res=""
#    for i in range (len(s)):
#        if s[i]>='0' and s[i]<='9':
#            res=res+str(i)
#    return res

#a=str(input())
#print (ps(a))

# def finddef(arr):
#    for a in arr:
#        good=1
#        k=a[0]
#        for i in range(0,len(a),+2):
#            if k!=a[i]:
#                good=0
#                break
#        print(good)
# a=list(map(str,input().split()))
# finddef(a)


# a=int(input())
# I=[]
# for i in range(a):
#     I.append(list(map(int,input().split())))
# s=0
# for i in I:
#     s+=i[0]
# d=0
# for i in I:
#     c=(i[0]*i[1]/100)+i[0]
#     v=c*i[2]/100
#     d +=c-v
#
# if(s>d):
#     print("Loss ",int(s-d))
# else:
#     print("Profit ",int(s-d))


#String Reverse
# def reverse(s):
#   str = ""
#   for i in s:
#     str = i + str
#   return str
#
s = "Geeksforgeeks"
print ("The original string  is : ")
print (s)
print ("The reversed string(using loops) is : ")
a=s.reverse()
print(a)


#Binary Search
# def BS(l,key):
#     low=0
#     high=len(l)-1
#     f= False
#     while low<=high and not f:
#         mid=(low+high)//2
#         if key==l[mid]:
#             f=True
#         elif key>l[mid]:
#             low=mid+1
#         else:
#             high=mid-1
#     if f==True:
#         print(f"Match of {key} is Found")
#     else:
#         print(f"Match of {key} is not Found")
#
# a=int(input("Enter the size of list: "))
# l=[int(input())for i in range(a)]
# l.sort()
# print (l)
# key=int(input("Enter Key : "))
# BS(l,key)


#Linear Search
# def LS(l,key):
#     f=False
#     l2=[]
#     for  i in range(len(l)):
#         if key==l[i]:
#             # print(f"{key} is found in position {i+1}")
#             f=True
#             l2.append(i)
#
#     if f==True:
#         for i in l2:
#             print(f"{key} is found in pos {i+1} ")
#     else:
#         print(f"{key} is not found ")
#
# a=int(input(" Enter the Size: "))
# l=[int(input())for i in range(a)]
# l.sort()
# print(l)
# key=int(input("Enter key value: "))
# LS(l,key)


#Matrix Manipulation
# r=int(input("Enter no of rows: "))
# c=int(input("Enter no of columns: "))
#
# print("Enter Elements for matrix 1: ")
# m1=[[int(input())for i in range(c)]for j in range(r)]
# print("Matrix 1 is: ")
# for i in range(r):
#     for j in range(c):
#         print(format(m1[i][j],">3"),end="")
#     print()
#
# print("Enter Elements for matrix 2: ")
# m2=[[int(input())for i in range(c)]for j in range(r)]
# print("Matrix 2 is: ")
# for i in range(r):
#     for j in range(c):
#         print(format(m2[i][j],">3"),end="")
#     print()
#
# res=[[0 for i in range(c)]for j in range(r)]
# print("The Answer is: ")
# for i in range(r):
#     for j in range(c):
#         res[i][j]=m1[i][j]-m2[i][j]
#         print(format(res[i][j],">3"),end="")
#     print()


# Matrix Multiplication
# p=int(input("Enter no of rows in m1: "))
# q=int(input("Enter no of columns in m2: "))
# n=int(input("Enter no of columns in m1 / Enter no of rows in n2: "))
#
# print("Enter Elements for matrix 1: ")
# m1=[[int(input())for i in range(n)]for j in range(p)]
# print("Matrix 1 is: ")
# for i in range(p):
#     for j in range(n):
#         print(format(m1[i][j],">5"),end="")
#     print()
#
# print("Enter Elements for matrix 2: ")
# m2=[[int(input())for i in range(q)]for j in range(n)]
# print("Matrix 2 is: ")
# for i in range(n):
#     for j in range(q):
#         print(format(m2[i][j],">5"),end="")
#     print()
#
# res=[[0 for i in range(q)]for j in range(p)]
# for i in range(p):
#     for j in range(q):
#         for k in range(n):
#             res[i][j]=res[i][j]+m1[i][k]*m2[k][j]
#
# print("The Multiplication is: ")
# for i in range(p):
#     for j in range(q):
#         print(format(res[i][j],">5"),end="")
#     print()
