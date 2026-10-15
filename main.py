
# Stock Inventory Management System
# Version 1.0

inventory = {}


def add_product():
    product_id = input("Product ID: ")

    if product_id in inventory:
        print("Product already exists!")
        return

    name = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Initial quantity: "))

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return

    inventory[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "reorder_level": 5
    }

    print("Product added successfully!")


def view_products():
    if not inventory:
        print("Inventory is empty.")
        return

    for product_id, product in inventory.items():
        print(
            f"ID: {product_id} | "
            f"Name: {product['name']} | "
            f"Price: Rs.{product['price']:.2f} | "
            f"Quantity: {product['quantity']}"
        )


def main():
    while True:
        print("""
--- STOCK INVENTORY SYSTEM ---
1. Add Product
2. View Products
3. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
