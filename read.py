# Stores the data from txt file in dictionary
def dictupdt(dict):
    file = open("laptop.txt","r")
    id = 1
    for i in file:
        i = i.replace("\n","")
        dict.update({id : i.split(",")})
        id += 1
    file.close()
    return dict

# returns shipping price for orders
def shipprice():
    ship_ = input("Do you want to ship the items?(y/n): ")
    
    if ship_ == "y" or ship_ =="Y":
        shipping = 1000
    
    else:
        shipping = 0

    return shipping 

# returns shipping price for sales
def shipcost(ship):
    if ship == "y" or ship =="Y":
        val = input("Do you live inside kathmandu valley?(y/n)")
        if val == "y" or val == "Y":
            shipcost = 150

        else:
            shipcost = 300   

    else:
            shipcost = 0     

    return shipcost
