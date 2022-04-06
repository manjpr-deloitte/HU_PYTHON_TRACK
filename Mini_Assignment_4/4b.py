lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
counting_a=list(map(lambda x:x.count("a"),lst1))
counting_A=list(map(lambda x:x.count("A"),lst1))
comb=list(map(lambda x,y:[x,y],counting_a,counting_A))
print(counting_a)
print(counting_A)
print(comb)

