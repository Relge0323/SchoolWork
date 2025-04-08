def display_inventory(inventory):
    print("\nYour Inventory:")
    for item in inventory:
        print(f"{item['name']} - Type: {item['type']}, Value: {item['value']}")


def add_item(inventory, name, item_type, value):
    inventory.append({"name": name, "type": item_type, "value": value})
    print(f"{name} has been added to your inventory!")


def sort_inventory(inventory, sort_by="name"):
    if sort_by == "name":
        inventory.sort(key=lambda x: x['name'])
    elif sort_by == "type":
        inventory.sort(key=lambda x: x['type'])
    elif sort_by == "value":
        inventory.sort(key=lambda x: x['value'], reverse=True)
    print(f"Your inventory has been sorted by {sort_by}!")



# Initialize inventory
inventory = [
    {"name": "Healing Potion", "type": "Potion", "value": 50},
    {"name": "Iron Sword", "type": "Weapon", "value": 10},
    {"name": "Mana Potion", "type": "Potion", "value": 30},
    {"name": "Steel Armor", "type": "Armor", "value": 40}
]

# display inventory
display_inventory(inventory)

# add a new item
add_item(inventory, "Fireball Scroll", "Spell", 100)

# sort by value
sort_inventory(inventory, "value")

display_inventory(inventory)