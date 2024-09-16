from computer import Computer
from typing import Dict, Optional


class ResaleShop:

    # What attributes will it need?
    inventory: list
    itemID: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                 inventory: list):
         self.inventory = inventory
         self.itemID = 0

    # What methods will you need?
    
    # Buy computer:
    def buy(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory.append(computer) # add computer to inventory
        print("Added", computer.description, "to inventory.") # conformation 
        return self.itemID
    
    
    # Print inventory:
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for i in self.inventory:
                # Print its details
                print(f'Item ID: {self.itemID} : {i.description}')
        else:
            print("No inventory to display.")
    
    # Refurbish computer:
    def refurbish(self, inventory:list, new_os: Optional[str] = None):
        if self.itemID in self.inventory:
            computer = self.inventory[self.itemID] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff
            
            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", self.itemID, "not found. Please select another item to refurbish.")
    
    # Update price:
    #def update_price():
        #
        
    # Sell Computer:
    #def sell(self):
        #

        

def main():
    # Example computer  
    example_com = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)    
    
    # Example computer list
    list_example = []

    # Add computers to resale shop
    resale_example = ResaleShop(list_example)
    resale_example.buy(example_com)
    resale_example.print_inventory()

    # Refirbish computer
    resale_example.refurbish(list_example,"IOS 15")
  
      
      
      



# Only run main() if I am running this program directly
if __name__ == "__main__":
    main()