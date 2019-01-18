our_items = ["T-shirt", "Sweater"]
n = input("choose: ")
if n == "R":
    print(*our_items, sep=", ")
elif n == "C":
    new_item = input("Enter new: ")
    our_items.append(new_item)
    print(*our_items, sep= ", ")
elif n == "U":
    update_position = int(input("Enter update position: "))
    new_item_2 = input("New item 2: ")
    our_items[update_position-1] = new_item_2
    print(our_items)
else:
    delete_position = int(input("Enter delete position: "))
    del our_items[delete_position-1]
    print(our_items)