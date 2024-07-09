import operations as os
import read as rd
import write as wr
import datetime
import random

dict = {}
subtotal = 0

# Title of shop
wr.namedisplay()
print("Hello Sir/Madam, WELCOME to Gadgets Nepal,")
print("")

loop = True
while loop == True :
    
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d") 
    time = now.strftime("%H:%M:%S")
    disc = random.randint(0,10)

    # stores the txt file in a dictionary
    dict = rd.dictupdt(dict)

    # gives options to user to operate the system
    wr.options()
    num = input("Enter: ")

    if num == "1":
        print("\n")
        # displays the stock the shop has
        os.displaystock()
        print("\n")
        input("Press enter to continue:")
#if user enters 2
    elif num == "2":

        name, addrs, number = os.userdetails()#returns the name,addrs,number entered by user
        sale = []
        cha = "y"
       
        while cha == "y" or cha == "Y":
            detail = [] 

            id = os.id(dict)#returns id after input and id validation  
            quantity = int(dict[id][9])#accessing the quantity of the model
            
            if quantity == 0:
                print("Model Out Of Stock, Please choose another laptop\n")
                continue
                
            
            print("Available Quantity : ",quantity)

            # returns quantity
            qty = os.qty(quantity)
            #appends the details entered in a list                
            sale,detail = os.saledetail(dict,id,sale,detail,qty)
            subtotal =  subtotal +  detail[4]
            dict[id][9] = quantity - qty
                
            cha = input("\nDo You want to buy more?(y/n): ")
        ship = input("Do you want to ship this laptop?(y/n): ")
        
        #shipping price
        shipcost = rd.shipcost(ship)

        billnum = random.randint(10000,1111111)
        vatno = random.randint(10000000,99999999)
        
        filename = f"sale_{now:%Y-%m-%d_%H-%M-%S_}"+str(billnum)+".txt"
        foldername = "salesbills"
        
        #billprinting
        wr.billname(billnum,vatno)
        os.billbody(name,addrs,number,date,time,sale,subtotal,shipcost,disc)
        os.billtxt(filename,foldername,billnum,name,addrs,number,sale,subtotal,shipcost,disc,"Gadgets Nepal","Kamaladi, Kathmandu, Nepal","9821345634",vatno,date,time)
        os.write(dict)
        subtotal = 0
        
            
    elif num == "3":
        loop1 = True
        while loop1 == True:
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d") 
            time = now.strftime("%H:%M:%S")

            wr.orderoptions()
            num = input("Enter : ")         

            if num == "1":                   
                ch = "y"
                sale1 = []
                subtotal1 = 0
                
                while ch == "y" or ch == "Y":

                    detail1 = []
                    #returns id entered
                    id = os.id(dict)
                    while True:
                        try:
                            qty1 = int(input("Enter The Quantity: ")) 
                            while qty1 <= 0 :
                                print("\n Invalid Quantity \n.")
                                qty1 = int(input("Enter a valid Quantity: "))
                            break
                        except ValueError:
                            print('Quantity cannot be String. Please enter a valid integer.\n')

                    #accessing the quanityt from dictionary
                    quantity = int(dict[id][9])
                    rate = int(dict[id][8])

                    finalq = quantity + qty1
                    #updating the quantity
                    dict[id][9] = finalq

                    sale1,detail1 = os.saledetail(dict,id,sale1,detail1,qty1)
                    subtotal1 =  subtotal1 +  detail1[4]

                    ch = input("Do you Want To Order More(y/n)? : ")

                billnum = random.randint(10000,1111111)
                vatno = random.randint(10000000,99999999)
                filename = f"order_{now:%Y-%m-%d_%H-%M-%S_}"+str(billnum)+".txt"
                foldername = "orderbills"
                                              
                shipping = rd.shipprice()#gives shipping price
                #billprinting
                wr.orderbillname(billnum,vatno)
                os.billbody("Gadgets Nepal","Kamaladi,Kathmandu","9821345634",date,time,sale1,subtotal1,shipping,disc)
                os.billtxt(filename,foldername,billnum,"Gadgets Nepal","Kamaladi,Kathmandu","9821345634",sale1,subtotal1,shipping,disc,"Jyoti Electronics(Pvt.) Ltd","Jamal, Kathmandu, Nepal","9841345678",vatno,date,time)

                subtotal1 = 0

                
            elif num == "2":
                sale1=[]
                subtotal1 = 0
                id1 = [*dict.keys()][-1] + 1
                chy = "y"
                while chy == "y" or chy == "Y":
                    detail1 = []
                    
                    #appends the custom order in the proddetail
                    proddetail,quant = os.update_order()
                    dict.update({id1 : proddetail})#adding custom order in dictionary
                    
                    sale1,detail1 = os.saledetail(dict,id1,sale1,detail1,quant)
                    subtotal1 = subtotal1 + detail1[4]

                    id1 += 1             
                    chy = input("\nDo you Want To Order More(y/n)? : ")

                billnum = random.randint(10000,1111111)
                vatno = random.randint(10000000,99999999)
                filename = f"customorder_{now:%Y-%m-%d_%H-%M-%S_}"+str(billnum)+".txt"
                foldername = "orderbills"
                                              
                shipping = rd.shipprice()#returns shipping price
                #bill printing
                wr.orderbillname(billnum,vatno)
                os.billbody("Gadgets Nepal","Kamaladi,Kathmandu","9821345634",date,time,sale1,subtotal1,shipping,disc)
                os.billtxt(filename,foldername,billnum,"Gadgets Nepal","Kamaladi,Kathmandu","9821345634",sale1,subtotal1,shipping,disc,"Jyoti Electronics(Pvt.) Ltd","Jamal, Kathmandu, Nepal","9841345678",vatno,date,time)
            
            
            elif num == "3":
                loop1 = False

            else :
                print("\n Option Out of Bounds")
                print(" Please enter a valid option")



            os.write(dict)

    elif num == "4":
        loop=False
        print("Thankyou for visiting!! Have a nice day")
    
    else :
        print("\nOption out of bounds. ")
        print("\n")

