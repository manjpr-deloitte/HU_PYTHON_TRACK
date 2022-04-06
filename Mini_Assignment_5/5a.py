lst=[-1000, 500, -600, 700, 5000, -90000, -17500]
print(list)
# negative=list(filter(lambda x : x<0,lst))
# result=list(map(lambda x:abs(x),negative))
# print("Negetive numbers are:",result)
negative=list(map(lambda x:abs(x),(filter(lambda x:x<0,map(lambda x:x,lst)))))
print(negative)
