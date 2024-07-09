
# info of customer
def userdetails():
    # asks the user for his information
    name = input("\nEnter your name: ")
    addrs = input("Enter your address : ")
    
    while True:
        try:
            number = int(input("Enter your phone number: "))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    return name,addrs,number
# id input and validation
def id(dict):
    while True:
        try:
            id = int(input("\nEnter the Id of laptop you want to buy: "))
            while id <= 0 or id > len(dict):
                print("\n Please enter a valid Id \n")
                id = int(input("Enter the Id of laptop you want to buy: "))
            break
        except ValueError:
            print('ID cannot be String. Please enter a valid integer.')
    
    return id

# quantity input and validation
def qty(quantity):
    while True:
        try:
            qty = int(input("\nEnter The Quantity: "))
            while qty > quantity or qty < 0:
                print("\n Quantity greater than available stock or invalid Input \n.")
                qty = int(input("Enter a valid Quantity: ")) 
            break
        except ValueError:
            print('Quantity cannot be String. Please enter a valid integer.')  

    return qty
# appends the custom order to dictionary
def update_order():
    
    proddetail = []
    company = input("\nCompany Name : ")
    model = input("Model Name : ")
    size = input("Display Size : ")
    refrate = input("Refresh Rate : ")
    cpu = input("Processor : ")
    ram = input("RAM : ")
    rom = input("Storage : ")
    graphics = input("Graphics : ")

    while True:
        try:
            rate = int(input("Price : "))
            break
        except ValueError:
            print('Price cannot be String. Please enter a valid integer.\n')

    while True:
        try:
            quant = int(input("Quantity : "))
            break
        except ValueError:
            print('Quantity cannot be String. Please enter a valid integer.\n')

    proddetail.append(company)
    proddetail.append(model)
    proddetail.append(size)
    proddetail.append(refrate)
    proddetail.append(cpu)
    proddetail.append(ram)
    proddetail.append(rom)
    proddetail.append(graphics)
    proddetail.append(rate)
    proddetail.append(quant)

    return proddetail,quant


def write(dict):
    file = open("laptop.txt","w")
    for i in dict.values():
        file.write(",".join(map(str,i))+"\n")
    file.close()


# stores the item purchased to display in bill
def saledetail(dict,id,sale,detail,qty):
    
    detail.append(dict[id][0])  
    detail.append(dict[id][1])
    detail.append(qty)
    detail.append(dict[id][8])
    rate = int(dict[id][8])
    amt = rate * qty
    detail.append(amt)

    sale.append(detail)

    return sale,detail

# displays the stock the shop has
def displaystock() :
    print(" Here are some laptop we currently have in stock: ")
    print("\n")
        
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N.   Company      Model \t Display Size   Refresh Rate        Processor       RAM \t    Storage \t    Graphics \t   Price(Rs) \t Quantity ")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

    file = open("laptop.txt","r")
    n = 1
    for line in file:
        print(n,"\t"+line.replace(",","\t    "))
        n = n+1

    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.close()


# generates the body of the bill
def billbody(name,addrs,number,date,time,sale,subtotal1,shipping,disc):
    print("\t Date : ",date ,"\t\t\tTime : ",time)
    print("\t Sold To: ",name)
    print("\t Address: ",addrs)
    print("\t Tel: ",number)
    print("\t---------------------------------------------------------------------")
    print("\t S.N.   company   Model \t QTY      Rate            AMOUNT(Rs.)")
    print("\t---------------------------------------------------------------------")

    n = 1
    for i in range(len(sale)):
        print("\n\t",n,"\t",end = "")
        n = n+1
        for j in range(len(sale[i])):
            print(sale[i][j],"\t  ",end = "")    

    # bottom part of the bill
    discamt = disc/100 * subtotal1
    discamt_float = "{:.2f}".format(discamt)

    taxable = int(subtotal1) - float(discamt_float)
    vat = 0.13 * taxable
    vat_float = "{:.2f}".format(vat)
    Grandtotal = "{:.2f}".format(taxable + float(vat_float) + shipping)

    print(" \n\n\n \t\t\t\t\t\tSub-total\t  ",subtotal1)
    print(" \t\t\t\t\t    Discount(",disc,"%)\t  ",discamt_float)
    print(" \t\t\t\t\t\t Shipping\t  ",shipping)
    print(" \t\t\t\t\t\t Taxable\t  ",taxable)
    print(" \t\t\t\t\t\t VAT 13%\t  ",vat_float)
    print("\t----------------------------------------------------------------------")
    print("\t         Thank You!                   Grand Total         ",Grandtotal)
    print("\t----------------------------------------------------------------------")
    print("\n")

# generates the bill in txt file
def billtxt(filename,foldername,billnum,name,addrs,number,sale,subtotal,shipcost,disc,shopname,address,cont,vatno,date,time):
    
    filepath = f"{foldername}/{filename}"
    file = open(filepath,"w")
    file.write("\n\n")

    # shopdetails
    if shopname == "Gadgets Nepal":
        file.write("\t \t \t \t \t        "+shopname+" \n")
        file.write("\t \t \t \t \t "+address+ "\n")
        file.write("\t\t\t\t         VAT NO : "+str(vatno)+"\n")
        file.write("\t \t \t \t \t     Contact - "+cont+"\n")
        file.write("\t \t \t \t \t        TAX INVOICE \n")
    else :
        file.write("\t \t \t \t       "+shopname+" \n")
        file.write("\t \t \t \t \t     "+address+ "\n")
        file.write("\t\t\t\t            VAT NO : "+str(vatno)+"\n")
        file.write("\t \t \t \t \t       Contact - "+cont+"\n")
        file.write("\t \t \t \t \t          TAX INVOICE \n")
        file.write("\n \t " + str(billnum) + "\n")

    # details of billing
    file.write("\n\t Date : "+ str(date) + "\t\t\t\t\tTime : " + str(time))
    file.write("\n\t Sold To: " + str(name))
    file.write("\n\t Address: " + str(addrs))
    file.write("\n\t Tel: " + str(number))
    file.write("\n\t---------------------------------------------------------------------")
    file.write("\n\t S.N.   company    Model          QTY      Rate        AMOUNT(Rs.)")
    file.write("\n\t---------------------------------------------------------------------")

    # items in bill
    n = 1
    for i in range(len(sale)):
        file.write("\n\t " + str(n) + "\t    ")
        n = n+1
        for j in range(len(sale[i])):
            file.write(str(sale[i][j]) + "\t   ")

    # discount and total
    discamt = disc/100 * subtotal
    discamt_float = "{:.2f}".format(discamt)
    taxable = int(subtotal) - float(discamt_float)
    vat = 0.13 * taxable
    vat_float = "{:.2f}".format(vat)
    Grandtotal = "{:.2f}".format(subtotal - discamt + shipcost + float(vat_float))
    file.write(" \n\n\n \t\t\t\t\t\t\t\tSub-total\t   " + str(subtotal))
    file.write(" \n\t\t\t\t\t\t          Discount(" + str(disc) + "%)\t   " + str(discamt_float))
    file.write(" \n\t\t\t\t\t\t\t\t Shipping\t   " + str(shipcost))
    file.write(" \n\t\t\t\t\t\t\t\t Taxable\t   " + str(taxable))
    file.write(" \n\t\t\t\t\t\t\t\t VAT 13%\t   " + str(vat_float))
    file.write("\n\t----------------------------------------------------------------------")
    file.write("\n\t         Thank You!                   Grand Total       " + str(Grandtotal))
    file.write("\n\t----------------------------------------------------------------------")
    file.write("\n")
    
    file.close()