def create_inventory(items):
    inventory = dict()
    for item in items:
        counter = 0
        for k in items:
            if item == k:
                counter += 1
                inventory[item]= counter  
    return inventory
    

def add_items(inventory, items):
    for item in set(items):
        if item in inventory:
            counter = items.count(item)
            inventory[item] += counter
        else:
            inventory[item] = items.count(i)
    return inventory

def decrement_items(inventory, items):
    for item in set(items):
        if inventory[item] != 0:
            inventory[item] -= items.count(i)
        if inventory[item] < 0:
            inventory[item] = 0
    return inventory


def remove_item(inventory, item):
    if item in inventory.keys():
         del inventory[item]
    return inventory


def list_inventory(inventory):
    new_list = []
    for k,v in inventory.items():
        if v > 0:
            new_list.append((k,v))
    return new_list