sal=int(input("ENTER your salary"))

home,edu,other=map(int,input("Enter the other expenses home,edu,other").split())

bal=sal-home-edu-other

print("Your balance is ",bal)