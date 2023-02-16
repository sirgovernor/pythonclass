x=1
marks=67
grades=89
amount =int(input("plz enter your amount"))
#if statement
if (x>0):
    print("the number is positive")
    print(4+10)
#if else statement
if marks>=60:
    print("you have passed")
else:
    print("you have failed")
#if else if statement
if grades<=29 and grades>=0:
    print("you have failed")
elif grades<=49 and grades>=30:
    print("you have passed the test")
elif grades<=79 and grades>=50:
    print("you have credit")
elif grades<=100 and grades>=80:
    print("you have distinction")
else:
    print("wrong input")

    #enrollemnt of the cars
if amount<=100000 and amount>=150000:
    print("you can afford a motorcycle")
elif amount<=150000 and amount>=500000:
    print("you can afford a toyota car")
elif amount<=500000 and amount>=1000000:
    print("you can afford a issuzu car")
elif amount<=1000000 and amount>=5000000:
    print("you can afford a mercedes car")
elif amount<=5000000 and amount>=9000000:
    print("you can afford a prado car")
else:
    print("you can afford a higher class car")

