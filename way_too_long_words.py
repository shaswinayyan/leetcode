n=int(input())
l=[]
for k in range(n):
    l.append(input())
for i in l:
    for j in i:
        if len(i)<=10:
            print(i)
        else:    
            x=str(len(i)-2)
            m=i[0]+x+i[-1]
            print(m)
        break