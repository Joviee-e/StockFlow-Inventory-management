
# Stock Inventory Management System
# Version 1.0

inventory = {}


def add_stock():
    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    quantity = int(input("Quantity to add: "))

    if quantity <= 0:
        print("Quantity must be positive!")
        return

    inventory[product_id]["quantity"] += quantity
    print("Stock updated successfully!")


def low_stock_report():
    print("\n--- LOW STOCK REPORT ---")
    found = False

    for product_id, product in inventory.items():
        if product["quantity"] <= product["reorder_level"]:
            print(
                f"{product_id} - {product['name']} "
                f"(Quantity: {product['quantity']})"
            )
            found = True

    if not found:
        print("No products require restocking.")

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
3. Add Stock
4. Low Stock Report
5. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            add_stock()
        elif choice == "4":
            low_stock_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()