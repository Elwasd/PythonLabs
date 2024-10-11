# #0 Ratio
# a = int(input("Enter your number "))
# if a == 0:
#     print("Error")
# else:
#     print(a<<1)


# a = int(input("Enter 1st number "))
# b = int(input("Enter 2nd number "))
# operation = input("choose operation(+,-,*,/) ")
#
# if operation == '+':
#     print("a+b = ", a+b)
# if operation == '-':
#     print("a-b = ", a-b)
# if operation == '*':
#     print("a*b = ", a*b)
# if operation == '/':
#     print("a/b = ", a/b)

# #1 Ratio
# a = int(input("Enter your number "))
# a1 = a%10000//1000
# a2 = a%1000//100
# a3 = a%100//10
# a4 = a%10
# if a1+a4 == a2-a3:
#     print("Yes")
# else:
#     print("No")

# #2Rodkomnaszor
# a = int(input("Enter your old"))
# if a >= 18:
#     print("Access is allowed")
# else:
#     print("Acsess denied")

# #3 Arithmetic progressino
# a1 = int(input("Fist number"))
# a2 = int(input("Second number"))
# a3 = int(input("Third number"))
# if a3 - a2 == a2 - a1:
#     print("YES")
# else:
#     print("NO")
#
# #4 Rook Move
#
# x1  = int(input("enter colum "))
# y1 = int(input("enter row"))
# x2  = int(input("enter colum to move "))
# y2  = int(input("enter colum  to move"))
# if  (x1==x2 or  y1==y2):
#     print("Yes")
# else:
#     print("NO")
#5 King's move
# x1  = int(input("enter colum "))
# y1 = int(input("enter row"))
# x2  = int(input("enter colum to move "))
# y2  = int(input("enter colum  to move"))
# if (x1==x2 or  y1==y2):
#     print ("Yes")
# elif (x1==x2 and  y1==y2):
#     print("Yes")


# #6 Average number
# a1 = int(input("enter your number"))
# a2 = int(input("enter your number"))
# a3 = int(input("enter your number"))
# r = []
# r.append(a1)
# r.append(a2)
# r.append(a3)
# r.sort()
# print(r[1])