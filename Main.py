import os
import tkinter as tk
import csv
from tkinter import messagebox, ttk

class Product:
    def __init__(self, name = "", price = 0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryApp(Product):
    def __init__(self,root):
        self.root = root
        self.root.title("Modern Inventory Tracking System")
        self.root.geometry("1000x800")
        self.inventory = []
        super().__init__(name="" , price=0 , quantity=0)

        #window style
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        style.map('Treeview', background=[('selected', '#34A2FE')])
        search_frame = tk.Frame(root, bg="#f0f0f0")
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(search_frame, text="Search Product:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame, width=30, font=("Arial", 12))
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_product, bg="#34A2FE", fg="white",font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Clear Search", command=self.clear_search, bg="#FF7F50", fg="white",font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(root, columns=("Name", "Price", "Quantity"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")



        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Button(button_frame, text="ADD Item", command=self.Add_Item, bg="#32CD32", fg="white",font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Product",command=self.Edit_Product,bg="#1E90FF", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Product", command=self.delete_product, bg="#DC143C", fg="white",font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Save Inventory", command=self.save_inventory, bg="#808080", fg="white",font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Inventory", command=self.restore_inventory, bg="#FF8C00", fg="white",font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.restore_inventory()


    def restore_inventory(self):
        if not os.path.exists('Inventory.csv') or os.stat('Inventory.csv').st_size == 0:
            messagebox.showinfo("Info", "No inventory data found.")
            return
        with open('Inventory.csv', 'r') as csvfile:
            self.tree.delete(*self.tree.get_children())
            self.inventory.clear()
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                name = row['Name']
                price = float(row['Price'])  # Convert price to float
                quantity = int(row['Quantity'])  # Convert quantity to int
                self.inventory.append(Product(name, price, quantity))
                self.tree.insert("", tk.END, values=(name, f"${price:.2f}", quantity))


    def Save_Inventory_in_Csv(self,item):
        file_exists = os.path.exists('Inventory.csv')
        with open('Inventory.csv', 'a', newline='') as csvfile:
            fieldnames = ['Name', 'Price', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists or os.stat('Inventory.csv').st_size == 0:
                writer.writeheader()

            # Write inventory data
            writer.writerow({'Name': item.name, 'Price': item.price, 'Quantity': item.quantity})
        messagebox.showinfo("Info", "Inventory saved to Inventory.csv!")
        return
    def Update_Inventory_in_CSV(self):
        file_exists = os.path.exists('Inventory.csv')
        with open('Inventory.csv', 'w+', newline='') as csvfile:
            fieldnames = ['Name', 'Price', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists or os.stat('Inventory.csv').st_size == 0:
                writer.writeheader()

            # Write inventory data
            for row in self.inventory:
                writer.writerow({'Name': row.name, 'Price': row.price, 'Quantity': row.quantity})
        messagebox.showinfo("Info", "Inventory has been updated!")



    def Add_Item(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Product")
        popup.geometry("300x600")

        tk.Label(popup, text="Name:", font=("Arial", 12)).pack(pady=5)
        name_entry = tk.Entry(popup, font=("Arial", 12))
        name_entry.pack(pady=5)

        tk.Label(popup, text="Price:", font=("Arial", 12)).pack(pady=5)
        price_entry = tk.Entry(popup, font=("Arial", 12))
        price_entry.pack(pady=5)

        tk.Label(popup, text="Quantity:", font=("Arial", 12)).pack(pady=5)
        quantity_entry = tk.Entry(popup, font=("Arial", 12))
        quantity_entry.pack(pady=5)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        def save_product():
            name = name_entry.get().strip()
            price = price_entry.get().strip()
            quantity = quantity_entry.get().strip()

            if not name or not price or not quantity:
                messagebox.showerror("Error", "All fields are required!")
                return
            try:
                price=float(price)
                quantity=int(quantity)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid Price or Quantity!")
                return
            item = Product(name, price, quantity)
            self.inventory.append(item)
            self.tree.insert("", tk.END, values=(name, f"${price:.2f}", quantity))
            popup.destroy()
            self.Save_Inventory_in_Csv(item)
        tk.Button(popup, text="ADD", command=save_product, bg="#32CD32", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=120, pady=10)

    def delete_product(self):
        selected_item=self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a product to delete.")
            return
        item=self.tree.item(selected_item)
        product_name=item["values"][0]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{product_name}'?")
        if confirm:
            self.inventory = [p for p in self.inventory if p.name != product_name]
            self.tree.delete(selected_item)
            self.Update_Inventory_in_CSV()

    def search_product(self):
        needed_item=self.search_entry.get().strip().lower()
        if not needed_item:
            messagebox.showerror("Error", "Please enter a product name to search.")
            return
        self.tree.delete(*self.tree.get_children())
        for item in self.inventory:
            if needed_item in item.name.lower():
               self.tree.insert("",tk.END, values=(item.name, f"{item.price:.2f}$", item.quantity))

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        for product in self.inventory:
            self.tree.insert("", tk.END, values=(product.name, f"${product.price:.2f}", product.quantity))

    def Edit_Product(self):
        needed_item=self.tree.selection()
        if not needed_item:
            messagebox.showerror("Error", "Please select a product name to update.")
            return
        selected_item=self.tree.item(needed_item)
        product_name = selected_item["values"][0]  # Name of the product
        product_price = selected_item["values"][1]  # Price of the product
        product_quantity = selected_item["values"][2]  # Quantity of the product
        popup = tk.Toplevel(self.root)
        popup.title("Update Product")
        popup.geometry("300x600")
        product_price = product_price.replace('$', '').strip()

        tk.Label(popup, text="Name:", font=("Arial", 12)).pack(pady=5)
        name_entry = tk.Entry(popup, font=("Arial", 12), justify='center')
        name_entry.insert(0, product_name)
        name_entry.pack(pady=5)

        tk.Label(popup, text="Price:", font=("Arial", 12)).pack(pady=5)
        price_entry = tk.Entry(popup, font=("Arial", 12), justify='center')
        price_entry.insert(0, product_price)
        price_entry.pack(pady=5)

        tk.Label(popup, text="Quantity:", font=("Arial", 12)).pack(pady=5)
        quantity_entry = tk.Entry(popup, font=("Arial", 12), justify='center')
        quantity_entry.pack(pady=5)
        quantity_entry.insert(0, product_quantity)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        unwanted_version=Product(product_name, product_price, quantity_entry)
        def save_product_after_edit():
            name = name_entry.get().strip()
            price = price_entry.get().strip()
            quantity = quantity_entry.get().strip()
            if not name or not price or not quantity:
                messagebox.showerror("Error", "All fields are required!")
                return
            try:
                # Convert price to float and quantity to int
                price = float(price)
                quantity = int(quantity)
            except ValueError:
                messagebox.showerror("Error", "Please enter valid values for price and quantity!")
                return
            new_item=Product(name, price, quantity)
            self.inventory = [p for p in self.inventory if p.name != product_name]
            self.inventory.append(new_item)
            self.tree.item(needed_item, values=(new_item.name, f'${new_item.price:.2f}', new_item.quantity))
            popup.destroy()
            self.Update_Inventory_in_CSV()
        tk.Button(popup, text="Update", command=save_product_after_edit, bg="#1E90FF", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=120, pady=10)

    def save_inventory(self):
        self.Update_Inventory_in_CSV()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

