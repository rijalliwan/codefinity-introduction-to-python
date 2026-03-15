# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")

for index in inventory:
   print(f"Processing {index}")
    
   current_stock = inventory[index][0]
   min_stock = inventory[index][1]
   restock_qnt = inventory[index][2]
    
   while current_stock<min_stock:
       current_stock+=restock_qnt
   inventory[index][0]=current_stock
    
   if current_stock> discount_threshold and inventory[index][3]== False:
       inventory[index][3]= True
    

    
    
    
   print("Processing completed") 