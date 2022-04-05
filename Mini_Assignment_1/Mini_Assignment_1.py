class StringClass:
    def __init__(self,demo):
        self.demo=demo
    def lis(self):
        return(list(self.demo))
    def length(self):
        return len(self.demo)
class PairsPossible(StringClass):
    def pair(self,test_list):
        res = [(n,object1) for idx,n in enumerate(test_list)for object1 in test_list[idx+1:]]
        print(res)

class SearchCommonElements(StringClass):
    def common(self,st,demo):
        a = list(set(st) & set(demo))
        print(a)
class EqualSumPairs:
    def pair2(self,test_list):
        res = [sum((int(n),int(object1))) for idx,n in enumerate(test_list) for object1 in test_list[idx+1:]]
        print(set(res))
        print(len(set(res)))
        
n=input("Enter a string :")
object1=StringClass(n)
print(object1.lis())
print(object1.length())
h=object1.lis()
object2=PairsPossible(object1)
object2.pair(h)
st=input("Enter string to compare ")
object3=SearchCommonElements(object1)
object3.common(n,st)
object4=EqualSumPairs()
object4.pair2(h)