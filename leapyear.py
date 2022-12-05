first=int(input("enter the first year"))
second=int(input("enter the future year"))
for year in range(first,second):
    if year%4==0 or year%400==0 and year%100!=0:
        printf("the leap years are ",i)