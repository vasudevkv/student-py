books={}
while True:
    print("1. purchase \n2. sale \n3.view \n4.search \n5.delete \n6.exit")
    ch=int(input("enter your choice:\n"))
    if(ch==1):
        ISBI=int(input("enter ISBI number:"))
        bookname=input('name:')
        price=int(input('price:'))
        author=input('author name:')
        quantity=int(input('enter quantity:'))
        book={ISBI:ISBI,'book name':bookname,'price':price,'author':author,'quantity':quantity,}
        books[ISBI]=book
        print(books)
    elif(ch==2):
        ISBI=int(input('enter ISBI number:'))
        sale=int(input("sale amount:\n"))
        if(ISBI in books):
            amt=books[ISBI]['quantity']
            if(sale>=amt):
                print("insufficent quantity ")
            else:
                balance=amt-sale
                books[ISBI]['quantity']=balance
                print("sussesfully saled")
    elif(ch==3):
       print(books)
    elif(ch==4):
        ISBI=int(input('enter ISBI number:'))
        if(ISBI in books):
         print(books[ISBI])
        else:
            print('no ISBI number')
    elif(ch==5):
         ISBI=int(input("enter delete ISBI number\n"))
         s=input("do you like to delete ISBI NUMBER yes or no")
         if(s=='yes'):
            del(books[ISBI]) 
            print('deleted sussesfully')
         else:
           print("thank you")
    else: 
       break
          
        
    


    
            
   
    

        




