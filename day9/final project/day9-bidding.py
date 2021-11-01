import os
def clear():
    os.system('cls')
def bid_winner(bidders={}):
    max=0
    for key in bidders:
        if bidders[key]>max:
            max=bidders[key]
    print(f"The winner is {key} with the best bet of {max}")
    
auctioners={}
endofauction=False
while not endofauction:
    name=input("What's your name:")
    bid=int(input("How much would you like to bid:$"))
    auctioners[name]=bid
    next_person=input("Are there any auctioners left?  yes/no\n")
    if next_person=="no":
        endofauction=True
        bid_winner(auctioners)
    elif next_person=="yes":
        endofauction=False
        clear()
