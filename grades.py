grades=float(input("enter you grade"))
if grades>=90:
    print("got an 'A'")
elif grades<=89 and grades>=75:
    print("you got 'B'")
elif grades<=74 and grades>=50:
    print("you got 'C'")
elif grades<=49 and grades>=30:
    print("you got 'D'")
else:
    print("you failed the test")

