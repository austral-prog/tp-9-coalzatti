def create_inventory(items):
    inventory = dict()
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] ==1
    return inventory

   


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] ==1
    return inventory
    
 


def decrement_items(inventory, items):
   for item in items:
        if item in inventory  and inventory > 0:
            inventory[item] -= 1
        return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    else:
        return inventory

def list_inventory(inventory):
     for item in items:
        if item in inventory  and inventory > 0:
            return [inventory]

