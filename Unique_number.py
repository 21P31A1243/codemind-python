num = int(input())
dictionary = {}
flag=0
while num > 0:
    remainder = num % 10
    if remainder in dictionary.keys():
        flag=1
        break
    else:
        dictionary[remainder] = True
    num = num // 10
    

if flag==1:
    print("Not Unique Number")
else:
    print("Unique Number")
        