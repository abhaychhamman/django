print("**************** WELCOME MY ATM****************************")

print("1. check balence?")
print("2. withdraw?")
a=input("enter your choice")

bal=500
opin=1010
if a==1:
    print("your balence is :",bal)
elif a==2:
    
    pin=input("enter pin")
    if pin==opin:
        amount=input("enter amount")
        if amount <= bal:
            bal=bal-amount
            print("Withdraw successfully!...........")
            print(bal)
        else :
            print("your amount is not sufficient!")
            




 