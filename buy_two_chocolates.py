prices=[1,2,2]
money=3
mon=money
chocolate=0
for i in range(len(prices)):
    if chocolate ==2:
        break
    elif prices[i]<=mon:
        chocolate+=1
        mon=mon-prices[i]
if chocolate!=2:
    mon=money
    chocolate=0    
print(chocolate)
print(mon)