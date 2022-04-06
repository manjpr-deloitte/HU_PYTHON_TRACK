from functools import reduce
n=int(input())
lst1=[]
while n!=0:
    x=int(input())
    lst1.append(x)
    n-=1
result=reduce((lambda x,y:x*y),lst1)
print(result)
