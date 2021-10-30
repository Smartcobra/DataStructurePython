# list= eval(input("Enter list :"))
# print(list)
# print(type(list))

# l=list(range(0,10,2))
# print(l)
# print(type(l))

# s="durga"
# l=list(s)
# print(l)
#
# s="Learning python is very easy"
# l=s.split()
# print(l)

########slice operator
###list2=list1[start:stop:step]
# n=[1,2,3,4,5,6,7,8,9]
# print(n[2:])
# print(n[2:4])
# print(n[2:8:2])

#################Traversing
# n=[0,1,2,3,4,5,6,7,8,9]
# i=0;
# while i<len(n):
#     print(n[i])
#     i=i+1

# n=[1,2,3,4,5,6,7,8,9]
# for i in n:
#     print(i)
#

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in n:
#     if i%2==0:
#         print(i)
#

l=["A","B","C"]
x=len(l)
for i in range(x):
    print(l[x-1-i])
    print (l[i])