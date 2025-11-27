#program to evaluate candiadate based on its technical HR and aptitude score.


apt=int(input("enter aptitude score"))

if(apt>=70):

    tech=int(input("Enter your technical score "))
    if(tech>=80):

        hr=int(input("Enter your HR score"))
        if(hr>=70):
            print("Selected for job")

        else:
            print("rejected in hr")
    else:
        print("Rejected in Technical  ")
else:
    print("Rejcected in Aptitude")


    




