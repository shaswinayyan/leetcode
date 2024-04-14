n=int(input())
count=0
while n>1:
    if n%2==0:
        count+=n/2
        n=n/2
    else:
        count+=int(n/2)
        n=int(n/2)+1
print(count)
        