accounts = {1210 : ["user1","24-08-2025","2408",10000],
            2891 : ["user2","16-04-2025","1234",20000],
            3675 : ["user3","24-09-2025",None,10000] 

            }
print("welcome")
while True:
    print("************************")
    print("1.withdraw")
    print("2.Deposit")
    print("3.pin Generation")
    print("4.Mini statement")
    print("5. Exit")
    x = int(input("Enter your option: "))
    if x >= 6:
        print("choose the correct option")
    else:
        if x ==1:
            accno = int(input("Enter Account Number : "))
            if accno not in accounts:
                print("No user exists with Account Number")
            else:
                if accounts[accno][-2] is None:
                    print("generate pin before withdraw operation")
                else:
                    pin = input("Enter Pin :")
                    if accounts[accno][-2] != pin:
                        print("Invalid pin,  Try again")
                    else:
                        amt = int(input("Enter Amount to withdraw:"))
                        if amt <= accounts[accno][-1]:
                            accounts[accno][-1] -= amt
                            print("Withdraw succss")
                        else:
                            print("Insufficient Fund/Balance/Amount")
                  
            
        elif x == 2:
             accno = int(input("Enter Account Number : "))
             if accno not in accounts:
                print("No user exists with Account Number")
             else:
                amt = int(input("Enter Amount to be Deposited:"))
                accounts[accno][-1] += amt
                print("Deposit Success")

        elif x == 3:
            accno = int(input("Enter Account Number : "))
            if accno not in accounts:
                print("No user exists with Account Number")
            else:
                if accounts[accno][-2] is not None:
                    print("Pin Already Generated")
                else:
                    pin = input("Enter Pin:")
                    cpin = input("Re enter pin: ")
                    if pin != cpin:
                      print("Pin Does not Match")
                    else:
                        accounts[accno][-2] = pin
                        print("Pin Generated Successully !")
            print(accounts )           
        elif x ==4:
            accno = int(input("Enter Account Number : "))
            if accno not in accounts:
                print("No user exists with Account Number")
            else:
                if accounts[accno][-2] is None:
                    print("generate pin before Mini statement operation")
                else:
                    pin = input("Enter Pin :")
                    if accounts[accno][-2] != pin:
                        print("Invalid pin,  Try again")
                    else:
                        print(f"Account Number: {accno}")
                        print(f"Name: {accounts[accno][0]}") 
                        print(f"Date of Birth: {accounts[accno][1]}")
                        print(f"Balance: {accounts[accno][-1]}")
        else:
            print("Thank you !")
        break
        
