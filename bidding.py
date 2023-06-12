bidding={}

def highest(bidding):
    winner=""
    high=0
    for i in bidding:
        if bidding[i]>high:
            high=bidding[i]
            winner=i
    print(f"highest bid is {high} and name is {winner}")



is_bidding=False
while not is_bidding:
    name = input("enter your name ")
    price = int(input("whats your price "))
    bidding[name]=price
    direction=input("enter yes or no ")
    if direction=="no":
        is_bidding=True
        highest(bidding=bidding)


