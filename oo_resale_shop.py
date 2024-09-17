# CSC 120 - Lily Ruddy
from computer import Computer
from typing import Optional


class ResaleShop:

    # What attributes will it need?
    # Attributes:
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
    def refurbish(self, computer, new_os: Optional[str] = None):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
            
            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", self.itemID, "not found. Please select another item to refurbish.")
    
    # Update price:
    def update_price(self, computer, new_price: int):
        if computer in self.inventory:
            computer.price = new_price # changes price to new price
        else:
            print("Item", computer.description, "not found. Cannot update price.")
        
    # Sell Computer:
    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer) # removes computer from the inventory
            print("Item", computer.description, "sold!")
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.")


        

def main():

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Example computer  
    example_com = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)  

    # Example computer list
    list_example = []

    # Add computers to resale shop
    resale_example = ResaleShop(list_example)
    resale_example.buy(example_com) # buys computer and adds to inventory
    resale_example.print_inventory()

    # Refirbish computer
    resale_example.refurbish(example_com, "IOS 16")
    print("New operating system:",example_com.operating_system)


    # Update price
    print(example_com.description, "is",example_com.price) # old price of computer
    resale_example.update_price(example_com, 1000)
    print(example_com.description, "is now",example_com.price) # new price

    # Sell computer
    resale_example.sell(example_com)

    # Print a little banner
    print("-" * 26)
    print("COMPUTER RESALE STORE PT 2")
    print("-" * 26)

    # Example computer 2  
    example_com2 = Computer("Mac Pro",
        "1.5 GHc 6-Core Intel Xeon E5",
        1018, 32,
        "macOS", 2000, 800)  
    
    # Testing error messages 
    resale_example.print_inventory() # error message for print_inventory
    resale_example.refurbish(example_com2, "IOS 10") # error message for refurbish
    resale_example.update_price(example_com2, 900) # error message for update_price
    resale_example.sell(example_com2) # error message for sell
    


# Only run main() if I am running this program directly
if __name__ == "__main__":
    main()