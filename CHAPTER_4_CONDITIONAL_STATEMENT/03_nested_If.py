#We can use condition within conndition using nested if else
#Second condition  depending on first and so on.
#To create second condition we have to provide nested intend level.

#EXAMPLE:>

age=int(input("Enter your age: "))

if(age>18 and age<30):
    per=int(input("Enter your percentage: "))

    if(per>=75):
        print("Form Accepted")

    else:
        print("Form rejected due to percentage")

else:
    print("form rejected due to age ")

    
    
