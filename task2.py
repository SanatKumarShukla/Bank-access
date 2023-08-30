import pickle
print("             Welcome to Bank Of Asaksa")
y=True
F=open(r"Transaction_history.txt","a+")
while True:
    print("1)Create account\n2)Access account\n3)Quit")
    e=int(input("Enter choice:"))
    if e==1:
        w=open(r"Account.dat","ab+")
        A=input("Enter your name:")
        B=int(input("Enter account no.:"))
        C=input("Create Passward:")
        D=input("Conform Passward:")
        while True:
            if C!=D:
                print("Wrong passward")
                C=input("Create Passward:")
                D=input("Conform Passward:")
            else:
                break
        E=int(input("Enter Balance:"))
        s={"Name":A,"Account_no.":B,"Passward":D,"Balance":E}
        pickle.dump(s,w)
        print("Account created successfuly")
        w.close()
    elif e==2:
        w=open(r"Account.dat","rb")
        A=int(input("Enter Account Number:"))
        B=input("Enter passward:")
        try:
            y=True
            while y:
                a=pickle.load(w)
                if a["Account_no."]==A and a["Passward"]==B:
                    print("_____________Welcome",a["Name"],"_________")
                    while True:
                        k=open(r"Account.dat","ab+")
                        print("What do you want to do:")
                        print("1)Check Balance\n2)Widhraw money\n3)Deposit money2\n4)Send Money\n5)Exit\n6)View Transaction History")
                        q=int(input("Enter choice:"))
                        if q==1:
                            print("Your balance is",a["Balance"])
                            F.write(str(["Balance was checked by",a["Name"]]))
                        elif q==2:
                            b=int(input("Enter the amount you want to widhraw:"))
                            c=a["Balance"]-b
                            if c>=0:
                                print("Amount widhrawn")
                                print("Remaining Balance:",c)
                                a["Balance"]=c
                                l=a
                                pickle.dump(l,k)
                                s=str([str(c)," Amount was widhrawn by",a["Name"]])
                                F.write(s)
                            else:
                                print("Insufficient Balance")
                                continue
                        elif q==3:
                            b=int(input("Enter the amount you want to deposit:"))
                            a["Balance"]=a["Balance"]+b
                            print("Amount deposited")
                            l=a
                            pickle.dump(l,k)
                            s=str([str(a["Balance"])," Amount was deposited by",a["Name"]])
                            F.write(s)
                        elif q==4:
                            l=int(input("Enter the Account Number of Reciver:"))
                            m=int(input("Enter money you want to send"))
                            c=a["Balance"]-m
                            if m>=0:
                                print("Amount sent")
                                print("Remaining Balance:",c)
                                a["Balance"]=c
                                pickle.dump(a,k)
                                try:
                                    while True:
                                        n=pickle.load(w)
                                        if n["Account_no."]==l:
                                           n["Balance"]=n["Balance"]+m
                                           p=n
                                           pickle.dump(p,k)
                                except EOFError:
                                    print()
                                s=str([a["Name"],"Sent",str(c)," Amount to",str(l)])
                                F.write(s)
                            else:
                                print("Insufficient Balance")
                                continue
                        elif q==5:
                            print("Loging off")
                            y=False
                            break
                        elif q==6:
                            F=open(r"Transaction_history.txt","r+")
                            r=F.read()
                            print(r)
                            F.close()
                        else:
                            print("Wrong input")
                else:
                    continue
        except EOFError:
            print("File not found")
            w.close()
    elif e==3:
        print("Thanks for visiting Asaksa Bank")
        break
F.close()         
        

                

