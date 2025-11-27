'''IN this statement if block denotes  TRUE while the condition is true
    if the condition is false the else block of code executes'''

#SYNTAX:>
'''
if(condition):
    (statement)
else:
    (statement)'''

#Example: To check person is eligible for driving or not 

age=int(input("Enter your age:\t"))

if(age>=18) and (age<80):
    print("Your eligible for driving\n ")

else:
    print("Your not Eligible for driving\n")

print("END OF PROGRAM")