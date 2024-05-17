class Products:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

        total_value = self.price * self.quantity
        print(f"Total value: {total_value}")

    def update_product_quantity(self, quantity_change):
        self.quantity = self.quantity + quantity_change

        print(f"Updated Quantity for {self.name}: {self.quantity}")


class ProductInventory():

    def __init__(self):

        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)
        print(f" The product '{product.name}' has been added to the product inventory.")

    def display_all_product(self):
        if not self.inventory:
            print("No product in the database.")
            return
        for product in self.inventory:
            product.display_info()
            print(f"Name: {product.name} | Quantity: {product.quantity}")
            print("-" * 20)

    def sumvalue(self):
        sumtotal_values = sum(product.quantity * product.price for product in self.inventory)
        print(f"The sun of total value of the inventory is: ${sumtotal_values: 2f}")
        print("-" * 20)

def main():
    p_inventory = ProductInventory()

    product1 = Products("A", 30, 10)
    product2 = Products("B", 20, 5)
    p_inventory.add_product(product1)
    p_inventory.add_product(product2)

    while True:
        print("\nPlease entry your selection:")
        print("1: Add a new product, 2: Display product information, 3: Update product quantity  4: The total value of inventory  0:Exit")

        choice = input("Choose an option (1/2/3/4/0): ")

        if choice == '1':

            name = input("Enter the name of the new product: ")
            price = int(input("Enter the price of the new product: "))
            quantity = int(input("Enter the quantity of the new product: "))
            new_product = Products(name, price, quantity)

            p_inventory.add_product(new_product)

        elif choice == '2':
            p_inventory.display_all_product()

        elif choice == '3':
            name = input("Enter product name to update: ")
            quantity_change = int(input("Enter quantity change (positive to restock, negative to sell): "))
            for product in p_inventory.inventory:
                if product.name.lower() == name.lower():
                    product.update_product_quantity(quantity_change)
                    break
            else:
                print("Product not found in inventory.")


        elif choice == '4':
            p_inventory.sumvalue()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
