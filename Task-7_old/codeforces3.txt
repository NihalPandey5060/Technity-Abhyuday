n,k=int(input().split())
scores=list(map(int,input().split()))
people=0
for i in range(n-k-1,n):
    if scores[k-1]<=0:
        print('0')
        break
    elif scores[i]>=scores[k-1]:
        people=people+1
print(people+k-1)        
