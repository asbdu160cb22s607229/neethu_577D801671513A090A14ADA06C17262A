year=int(input("enter a year:"))

if(year%4==0and year%100!=0)or(year%400==0):
  print(year,"is aleap year.")
else:
  print(year,"is not a leap year.")