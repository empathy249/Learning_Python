from clear_function import clear

def announce_winner():
      bidderCount = 0 
      highestBid = 0 
      highestBidderName = ""
      for currentBidder in bid_log:
            bidderCount += 1
            currentBid = bid_log[currentBidder]
            if currentBid >= highestBid:
                  highestBid = currentBid
                  bidderIsHighest = True
            else: 
                  bidderIsHighest = False
            if bidderIsHighest == True: 
                  highestBidderName = currentBidder
      print (f"There were {bidderCount} people who bid for the satellite")
      print (f"The highest bid was ${highestBid}")
      print (f"The highest bid of ${highestBid} was from {highestBidderName}")
      
satellite_art = """

==================-+-+-+-+-+-+-+-+-+-+==================
   ++++++\ /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//++++++
          \_______ .  .  .  .  .  .  ._______/
                 \_______ oooo _______/
                    |    \||||/    |
                    |    [++++]    |
                   }:{    |><|    }:{
                        (((II)))
                          /::\\'
                          \::/
                           ||
                      (((((oo)))))
                           !!
                           YY
                           /\\'
                          /><\\'
               !----------|UU|----------!
               |__________\  /__________|
                           ++
"""

print(satellite_art)
want_to_bid = input("Satellite for auction: Would you like to bid? Y or N: ").lower()
bid_log = {}
bid_again = True
bid_count = 0 
while bid_again == True:
      if want_to_bid == "y" and bid_count == 0:
            name = input("What is your name? ")
            bid_value = int(input("What is your bid $"))
            bid_log[name] = bid_value
            bid_again = True
            bid_count = 1
      elif want_to_bid == "y" and bid_count != 0: 
            further_bids = input("Bid Again? Y or N: ").lower()
            if further_bids == "y":
                  name = input("What is your name? ")
                  bid_value = int(input("What is your bid $"))
                  bid_log[name] = bid_value
            elif further_bids == "n":
                  bid_again = False
                  announce_winner()
      elif want_to_bid == "n":
            clear()
            print(satellite_art)
            want_to_end_bid = input("End auction? Y or N: ").lower()
            if want_to_end_bid == "y":
                  bid_again = False
                  announce_winner()
            elif want_to_end_bid == "n":
                  bid_again = True
      else: 
            clear()
            print("Sorry invalid input")

print(bid_log)