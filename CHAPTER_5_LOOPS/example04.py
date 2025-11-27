#Search for number x in this tuple

#Warning this example contains Tuple topic


num=(1,4,9,16,25,36,49,64,81,100)

x=81

i=0

while i<len(num):
    if(num[i]==x):
        print("the element has been found at index",i)
        
    else:
        print("Finding")
    i+=1
