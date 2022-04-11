import random
import string


while True:
    ch=int(input("1 : Play , 2 : Exit ---- "))

    rc = random.choice(range(1,100))

    if ch == 1:

        atps = 0

        while True:
            print()
            print("---------------------------------------------------")
        
            num = int(input("Guess the Number : "))
            atps+=1
            print("---------------------------------------------------")
            print()
    
            if num > rc:
                print("Lower Number Please...!!")
                

            elif num<rc:
                print("Higher Number Please...!!")
               
            elif num == rc:
                print("Right Guess")
                print()
                print("You Gussed the Right Number in : ",atps ,"Attempts")
                print("---------------------------------------------------")

                cg=input("Want to continue : Y/N ---- ")
                if cg.upper()=='Y':
                    pass
                
                elif cg.upper()=='N':
                    print()
                    print("---------------------------------------------------")
                    break
                
                else:
                    print("Invalid choice")

                

    elif ch==2:
        print()
        print("---------------------------------------------------")
        print("Thank You")
        print("---------------------------------------------------")
        break

    else:
        print("Invalid Choice")
