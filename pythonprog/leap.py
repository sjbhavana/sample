# to determine wether the year is leap or not

year=int(input("enter the year:"))
if(year%4==0 or  year%400==0):
    print(year ," is a leap year")
else:
    print(year, "not a leap year")
