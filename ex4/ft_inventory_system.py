import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")

    inventory = {}

    for args in sys.argv[1:]:
        parts = args.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{args}'\n")
            continue

        item = parts[0]
        quantity_text = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding\n")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}' : '{error}'\n")
            continue

        inventory.update({item: quantity})

    print(f"Got inventory: {inventory}\n")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}\n")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item)} items: {total_quantity}\n")

    for i in item_list:
        quantity = inventory[i]
        percentage = round((quantity/total_quantity) * 100, 1)
        print(f"Item {i} represents {percentage}%")

    print("\n")
    most_item = item_list[0]
    least_item = item_list[0]
    for i in item_list:
        if inventory[i] > inventory[most_item]:
            most_item = i
        if inventory[i] < inventory[least_item]:
            least_item = i

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )

    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )

    inventory.update({"magic_item": 1})

    print("Updated inventory:", inventory)
