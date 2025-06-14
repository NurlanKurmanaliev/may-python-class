limit=int(input("Enter limit: "))

first=0
second=1
print(first) # 0, 0
print(second) # 1, 1
next=first + second # 0+1

while next < limit:
    print(next) # 1, 2, 3
    first=second # 1, 1,2
    second=next # 1, 2,3
    next=first+second # 1+1=2 ; 1+2=3 ; 2+3=5 etc.





