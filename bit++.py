n=int(input())
x=0
for i in range(n):
    str_input=str(input())
    if str_input=="++X"or "X+++":
        x+=1
    elif str_input=="--X"or "X--":
        x-=1
print(x)