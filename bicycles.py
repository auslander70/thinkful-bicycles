""" Model the bicycle industry """


from random import randint


class Bicycle(object):
    """ Bicycle object.
    
    Args:
        model_name: string
        weight: float
        production_cost: float
    
    """
    
    def __init__(self, model_name, weight, production_cost):
        self.model_name = model_name
        self.weight = weight
        self.production_cost = production_cost
        
        
class BikeShop(object):
    """ Bicycle shop object.
    
    Args:
        shop_name: string
        inventory: dict
        margin: float (percentage)
    """
    
    def __init__(self, shop_name, inventory, margin, profit = 0.0):
        self.shop_name = shop_name
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
        

    def print_inventory(self):
        print('{} has the following bicycles in stock: '.format(self.shop_name))
        for bike in self.inventory:
            print(bike.model_name, self.inventory[bike])

        
    def print_profit(self):
        print('{} profits:  ${}'.format(self.shop_name, self.profit))

    def reset_profit(self):
        self.profit = 0.0
        
    def sell_bike(self, bike):
        self.inventory[bike] -= 1
        self.profit += bike.production_cost * self.margin
        return bike
        
        
class Customer(object):
    """ Customer object.
    
    Args:
        customer_name: string
        funds: float
        can_own: boolean
        bikes_owned: dict, key = Bicycle(),
                           value = int
    """
    
    def __init__(self, customer_name, funds, can_own = True):
        self.customer_name = customer_name
        self.funds = funds
        self.can_own = can_own
        self.bikes_owned = {}
        
    
    def purchase_bike(self, bike, store):
        if self.can_own:
            if store.inventory[bike] > 0:
                if self.funds > bike.production_cost:
                    self.funds -= (bike.production_cost * (1 + store.margin))

                    try:
                        self.bikes_owned[bike]
                    except KeyError:
                        self.bikes_owned[bike] = 0
                
                    self.bikes_owned[bike] += 1
        
                    print('{} has purchased a shiny new {} bicycle!'.format(
                                                        self.customer_name,
                                                        bike.model_name))
                    print('{} has {} dollars left in their bicycle fund'.format(
                                                        self.customer_name,
                                                        self.funds))            
            
                    store.sell_bike(bike)
                else:
                    print('{} doesn\'t have enough money to purchase a {} bicycle.'.format(
                                                        self.customer_name,
                                                        bike.model_name))
            else:
                print('{} doesn\'t have any {} bicycles in stock, sorry {}.'.format(
                                                        store.shop_name,
                                                        bike.model_name,
                                                        self.customer_name))
        else:
            print('{} can\'t own a bicycle.'.format(self.customer_name))
    
    
    def print_bikes_owned(self):
        for k in self.bikes_owned:
            print('{} owns {} {} bicycles.'.format(self.customer_name, self.bikes_owned[k], k.model_name))
    
        
        
def CalculateAffordableBikes(customers, store):
    """ For each customer, show bikes they can afford at a store.
    
    Args:
        customers: list of Customer objects
        store: BikeShop object
        
    Returns:
        affordable_bikes: dict, key = Customer,
                                value = list of affordable bikes
    """
    affordable_bikes = {}
    for customer in customers:
        affordable_bikes[customer] = []
        for bike in store.inventory:
            if (bike.production_cost * (1 + store.margin)) < customer.funds:
                affordable_bikes[customer].append(bike)
                
    return affordable_bikes
    
        
def DisplayAffordableBikes(affordable_bikes):
    """ Print customers and the bikes they can afford.
    
    Args:
        affordable_bikes: dict, key = Customer object,
                                value = list of Bicycle objects
    
    Returns:
        nothing.
    """
    
    for customer in affordable_bikes:
        print('{} can afford the following bicycles: '.format(
            customer.customer_name))
        for bike in affordable_bikes[customer]:
            print(bike.model_name)
        print()
        
        
def GenerateRandomInventory(bikes, minimum = 0, maximum = 10):
    """ Given a list of bicycles, generate an inventory dict.
    
    Args:
        bikes: list of bicycle classes
        minimum: minimum inventory (defaults to 0)
        maximum: maximum inventory (defaults to 10)
        
    Returns:
        inventory: dict, key = bicycle class name
                         value = number in stock
    """
    
    inventory = dict([bike, randint(minimum, maximum)] for bike in bikes)
        
    return inventory
           


 
    
    
    