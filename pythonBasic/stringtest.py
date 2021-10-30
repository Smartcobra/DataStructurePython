
# s='abcdef'
# print(s[0]) ## a
# print(s[4]) ## e
# print (s[-1])  ##f

s1='learning python is very easy'
# n=len(s1)
# i=0
# print ('forward direction')
# while i<n:
#     print(s1[i],end='')
#     i +=1
# print ('-----over---')
# l=-1
# print('backword direction')
# while l>=-n:
#     print(s1[l],end='')
#     l=l-1
# print ('----over--')

for i in s1:
    print(i,end='')
print()
for i in s1[::-1]:
    print(i,end='')
