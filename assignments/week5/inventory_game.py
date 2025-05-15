# --- Game State ---
inventory = []
MAX_INVENTORY_SIZE = 5

items_in_room = [
    {"name": "Tray", "type": "tool", "description": "Holds your items."},
    {"name": "Plate", "type": "tool", "description": "Holds your food."},
    {"name": "Spoon", "type": "tool", "description": "For eating your lunch and/or your dessert."},
    {"name": "Fork and knife", "type": "tool", "description": "For eating your lunch."},
    {"name": "Coffee", "type": "drink", "description": "Wakes you up."},
    {"name": "Wallet", "type": "tool", "description": "Use it to pay for your food."},
    {"name": "Food option 1", "type": "food", "description": "Pasta bolognesa."},
    {"name": "Food option 2", "type": "food", "description": "Tomato soup."},
]

tray = False
plate = False
paid = False

# --- Functions ---

def show_inventory():
    if len(inventory) == 0:
        print("Inventory empty.")
    else:
        print("Your inventory:")
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")

def show_room_items():
    if len(items_in_room) == 0:
        print("Mensa is empty.")
    else:
        print("In Mensa you can find:")
        for item in items_in_room:
            print(f"- {item['name']} ({item['type']})")

def pick_up(item_name):
    global tray, plate
    item_name_lower = item_name.lower()

    if tray == False and item_name_lower != "tray":
        print("You can't carry any item without the tray.")
        return

    if item_name_lower == "tray":
        tray = True

    if (item_name_lower in ["food option 1", "food option 2"]) and plate == False:
        print("You need a plate to get your food.")
        return

    if item_name_lower == "plate":
        plate = True


    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("You can't carry any more items.")
        return

    for item in items_in_room:
        if item['name'].lower() == item_name:
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You picked up the {item['name']}.")
            return
    print(f"There is no {item_name} here.")

def drop(item_name):
    for item in inventory:
        if item['name'].lower() == item_name:
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You dropped the {item['name']}.")
            return
    print(f"You don't have a {item_name} to drop.")

def use(item_name):
    global tray, plate, paid

    for item in inventory:
        if item['name'].lower() == item_name:

            if item['name'] == "plate":
                print(f"You can choose a food option from the menu.")
                inventory.remove(item)

            if item['name'].lower() == "food option 2":
                if "Spoon" in [i['name'] for i in inventory]:
                    print("You can eat your tomato soup with your spoon.")
                    inventory.remove(item)
                    return
                else:
                    print("You can't eat the Tomato Soup. You don't have the right utensils.")
                    return

            if item['name'].lower() == "food option 1":
                if "Fork and knife" in [i['name'] for i in inventory]:
                    print("You can eat your pasta with your fork and knife.")
                    inventory.remove(item)
                    return
                else:
                    print("You can't eat the Pasta. You don't have the right utensils.")
                    return

            if item['name'].lower() == "wallet":
                if paid:
                    print("You already paid for your food.")
                else:
                    paid = True
                    print("You paid for your food, enjoy!")
                return
        
            if item['name'].lower() == "coffee":
                print("Good choice to survive the next class")
            return

    print(f"You don't have a {item_name} to use.")

def examine(item_name):
    # Check in inventory
    for item in inventory + items_in_room:
        if item['name'].lower() == item_name:
            print(f"{item['name']}: {item.get('description', 'No description available.')}")
            return
    print(f"There is no {item_name} to examine.")

# --- Game Loop ---

def game_loop():
    print("Lunch at Mensa. Get your food.")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()