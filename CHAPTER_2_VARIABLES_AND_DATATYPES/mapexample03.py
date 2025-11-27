days=int(input("Enter the number of days ypu want to stay"))
res=int(input("enter the rent"))

car,driver,other=map(int,input("ENTER THE CAR AND DRIVER AMOUNT AND OTHER EXPENSES").split())

bill=res*days+car*days+driver*days+other+days

print("YOur total bill for trip is :",bill)


