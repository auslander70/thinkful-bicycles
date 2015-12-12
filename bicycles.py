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
        
        
    def affordable_bikes(self, BikeShop):
        bikes = []
        for bike in BikeShop.inventory:
            price = (bike.production_cost * BikeShop.margin) + bike.production_cost
            if BikeShop.inventory[bike] > 0 and price < self.funds:
                bikes.append(bike)
        return bikes
    
    
    def print_affordable_bikes(self, BikeShop):
        print('{} can afford the following bikes: '.format(self.customer_name))
        for bike in self.affordable_bikes(BikeShop):
            print(bike.model_name)
        
        
    def purchase_bike(self, bike, store):
        if not self.can_own:
            return('{} can\'t own a bicycle.'.format(self.customer_name))
        elif not store.inventory[bike] > 0:
            return('{} doesn\'t have any {} bicycles in stock, sorry {}.'.format(
                                                    store.shop_name,
                                                    bike.model_name,
                                                    self.customer_name))
        elif  not self.funds > bike.production_cost:
            return('{} has {} dollars left in their bicycle fund'.format(
                                                    self.customer_name,
                                                    self.funds))    
        else:
            self.funds -= (bike.production_cost * (1 + store.margin))
            self.bikes_owned[bike] = self.bikes_owned.get(bike, 0) + 1
            print('{} has purchased a shiny new {} bicycle!'.format(
                                                    self.customer_name,
                                                    bike.model_name))
            print('{} has {} dollars left in their bicycle fund'.format(
                                                    self.customer_name,
                                                    self.funds))            
            store.sell_bike(bike)

    
    def print_bikes_owned(self):
        for k in self.bikes_owned:
            print('{} owns {} {} bicycles.'.format(self.customer_name, self.bikes_owned[k], k.model_name))

        
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
           


 
    
    
    