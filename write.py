# display shopname
def namedisplay():
    print("\n\n")
    print("\t \t \t \t \t \t \t \t \t \t Gadgets Nepal")
    print("\t \t \t \t \t \t \t \t \t Kamaladi, Kathmandu, Nepal")
    print("\t \t \t \t \t \t \t \t \t      Contact - 9821345634")
    print("\n")

# displays the shopname in bill with different spacing
def billname(billnum,vatno):
    print("\n\n")
    print("\t \t \t \t  Gadgets Nepal")
    print("\t\t\t   Kamaladi, Kathmandu, Nepal")
    print("\t\t\t       VAT NO : ",vatno)
    print("\t \t \t       Contact - 9821345634")
    print("\t \t \t           TAX INVOICE\n")
    print("\t ",billnum,"\n")

# options user has to operate the system
def options():
    print("\nPlease, Choose the following options to operate the system: ")
    print(" 1: To View Stock")
    print(" 2: To Buy Laptop")
    print(" 3: To Order Laptops")
    print(" 4: To Exit")

# options for ordering
def orderoptions():
    print("\n1 : To increase available stock ")
    print("2 : To order a new model ")
    print("3 : TO EXIT ")

# title for order bill
def orderbillname(billnum,vatno):
    print("\n\n")
    print("\t \t \t      Jyoti Electronics(Pvt.) Ltd")
    print("\t \t \t        Jamal, Kathmandu, Nepal")
    print("\t\t\t           VAT NO : ",vatno)
    print("\t \t \t          Contact - 9841345678")
    print("\t \t \t             TAX INVOICE\n")
    print("\t ",billnum,"\n")