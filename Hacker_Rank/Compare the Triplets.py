a=list(map(int,input().split()))
b=list(map(int,input().split()))
alice=0
bob=0
c=len(a)
for i in range(c):
        if a[i]>b[i]:
                alice=alice+1
        elif a[i]<b[i]:
                bob=bob+1
        else:
                alice,bob=alice,bob


print(alice,bob)
