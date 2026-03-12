#mylist  = ["prashant" , "ashish" , "komal" , "ankush","ashish" , 77 ,"sandeep" ,60.35 , "prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1])

# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist.append('harsh')
# mylist.append("lakshman")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("sandeep")
# print(mylist)

# newlist = mylist.copy()
# print(mylist)
# print(newlist)

# mylist = [['prashant', 'jha'] , ['85.33'], [440022 , 'yyy']]
# print("example of ")
# #print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["prashant" , "jha"]
# print(list1*2)

#list2 = [50,25.5]
# print(list1+list2)

# list2 =[50,25.50, 'prashant']
# del list3
# print(list3)

# list2.clear()
# print(list2)

# name = 'kshitij' 
# print(name)
# myname = list(name)#typecasting
# print(myname)
# mylist =[44,33,55,0,9,88]
# mylist.sort()
# print(mylist)

# math=50 #fundamental datatypes is already extist it assingn the same address as we use temp memory
# phy = 50
# print(id(math)) #id returns address
# print(id(phy)) 

#looping
# for i in range(5,0,-1 ):
#     print(i)

# for i in range(1, 21):
#     for n in range(1, 11):
#         print(i * n, end="\t")
#     print()

#     if i == 10:
#         print("------")


#simple if 
#WAP to accept any digit and check that pos , neg , zero
# no = int(input("Enter any digit :"))
# if no>0:
#     print('positive')

# if no<0:
#     print('negetive')

# if no==0:
#     print('zero')    

#WAP to accept days and check the working days and weekends
# day = ""

# while day != "exit" or "EXIT":
#     day = input("Enter the day (or type exit to stop): ").lower()

#     if day == "saturday"or"SATURDAY" or day == "sunday" or "SUNDAY":
#         print("It is a Weekend")

#     elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
#         print("It is a Working Day")

#     elif day != "exit":
#         print("Invalid day entered")

#WAP to accept three paper marks and calculate total ,percentage and if percentage is graeter then equal to 60 then he/she is eligible

# m1 = float(input("Enter marks of Paper 1: "))
# m2 = float(input("Enter marks of Paper 2: "))
# m3 = float(input("Enter marks of Paper 3: "))

# total = m1 + m2 + m3
# percentage = total / 3

# print("Total Marks =", total)
# print("Percentage =", percentage)

# if percentage >= 60:
#     print("Eligible for Placement")
# else:
#     print("Not Eligible for Placement")


#WAP to accept five differnt value in 5 different var and check max value and print by using "simple is statement"
# WAP to accept five different values and check the maximum value using simple if

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# d = int(input("Enter fourth value: "))
# e = int(input("Enter fifth value: "))

# max_val = a

# if b > max_val:
#     max_val = b
# if c > max_val:
#     max_val = c
# if d > max_val:
#     max_val = d
# if e > max_val:
#     max_val = e

# print("Maximum value is:", max_val)

# # WAP to accept five values and print maximum value

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# d = int(input("Enter fourth value: "))
# e = int(input("Enter fifth value: "))

# max_val = max(a, b, c, d, e)

# print("Maximum value is:", max_val)