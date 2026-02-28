stocks={"aapl":180,"tsla":250,"microsoft":182,"amazon":200,"netflix":230,"meta":210,"google":280,"intel":170,"garena":120,"one8":190,}
totinv=0
file=open("stocks.txt","w")
def stk():
    inp=input("enter the name of the company in which you want to invest in stocks :").lower()
    if inp not in stocks:
        print("invalid stock name")
        return
    quan=eval(input("enter the amount of stocks do you want to invest :"))
    inv=stocks[inp]*quan
    file.write(f"stock :{inp}\n")
    file.write(f"stock quantity :{quan}\n")
    file.write(f"investment :{inv}\n")
    return inv
ask=input("do you want to invest in stocks(yes/no) :")
if ask.lower()!="yes":
        print("Thank you.bye")
else:
    print("current stocks and prices are as ")
    print("aapl:180,tsla:250,microsoft:182,amazon:200,netflix:230,meta:210,google:280,intel:170,garena:120,one8:190")
    print()
    inv=stk()
    totinv+=inv
    while(True):
        ask=input("do you want to invest in stocks again(yes/no)")
        if ask=="no":
            break
        if ask.lower()!="no":
            inv=stk()
            totinv+=inv
    file.write(f"total investment{totinv}")
    file.close()
    print("your total investment in stocks is :",totinv)
    print("Thank you.bye")


    
