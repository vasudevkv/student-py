accounts={}
while True:
    print("1 create account\n 2 view\n 3 search\n 4 deposite\n 5 withdraw\n 6 delete \n 7 exit")
    ch=int(input("enter your choice\n"))
    if(ch==1):
        accno=int(input("account number:"))
        name=input("name:")
        account=int(input("amount:"))
        account={accno:accno,'name':name,'amount':account}
        accounts[accno]=account
        print(accounts[accno])
    elif(ch==2):
        print(accounts)
    elif(ch==3):
        accno=int(input("enter accno\n"))
        if(accno in accounts):
            print(accounts[accno])
        else:
            print("no such account")
    elif(ch==4):
        accno=int(input("enter accno\n"))
        deposit=int(input("enter your deposite"))    
        if(accno in account):
            amt=account.get('amount')
            amt+=deposit
            account[accno]['amount']=amt
            print("deposite sussesful")
        else:
            print("no such account")
    elif(ch==5):
        accno=int(input("enter account\n"))
        withdraw=int(input("enter withdraw amount"))
        if(accno in account):
            amt=account[accno]['amount']
            if(withdraw>=amt):
                print("sorry insufficent balance")
        else:
            balance=amt-withdraw
            account[accno]['amount']=balance
            print("withdraw sussesful")
    elif(ch==6):
        accno=int(input("enter delete accno\n"))
        if(accno in account):
            s=input("did you want to delete this account say yes or no")
            if(s=='yes'): 
                del(account[accno])
                print("deleted account sussesfully")
            else:
                print("thank you")
        else:
            print("no such account")
    else:
        break;              
