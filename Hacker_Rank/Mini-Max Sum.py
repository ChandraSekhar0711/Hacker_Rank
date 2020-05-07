l=[]
l=list(map(int,input().split()))
s=sorted(l)
k=sum(l)
k1=sum(l)-min(l)
k2=sum(l)-max(l)
print(k2,k1)
