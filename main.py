import bicycles as bicycles

# let's make some bikes!
sticky_premium = bicycles.Bicycle('Sticky Premium', 1.4, 600.00)
sticky_premium_limited = bicycles.Bicycle('Sticky Premium Limited', 1.4, 800.00)
stainless_racer = bicycles.Bicycle('Stainless Racer', 1.2, 700.00)
touring = bicycles.Bicycle('Touring', 1.6, 400.00)
small_wheel = bicycles.Bicycle('Small Wheel', 1.3, 100.00)
rumbler_city = bicycles.Bicycle('Rumbler City', 1.9, 500.00)
    
inventory_bikes = [sticky_premium, sticky_premium_limited, stainless_racer,
                   touring, small_wheel, rumbler_city]
                       
inventory = bicycles.GenerateRandomInventory(inventory_bikes, 1, 4)
    
# brick and mortar brick and mortar! (let's make a bike shop)
cherubim = bicycles.BikeShop('Cherubim', inventory, 0.2)
    
# create some customers
customer1 = bicycles.Customer('Rudy', 200.0)
customer2 = bicycles.Customer('Alphonse', 500.0)
customer3 = bicycles.Customer('Rich Uncle Pennybags', 1000.0)
customer_list = (customer1, customer2, customer3)

# shop inventory
cherubim.print_inventory()
print()

# get affordable bikes    
affordable_bikes = bicycles.CalculateAffordableBikes(customer_list, cherubim)
bicycles.DisplayAffordableBikes(affordable_bikes)
    
# buy a bike alphonse
customer2.purchase_bike(small_wheel, cherubim)
    
# your turn poor Rudy
customer1.purchase_bike(small_wheel, cherubim)
    
# whatever mr. moneybags
customer3.purchase_bike(sticky_premium_limited, cherubim)

# shop inventory
cherubim.print_inventory()

# shop profit
cherubim.print_profit()