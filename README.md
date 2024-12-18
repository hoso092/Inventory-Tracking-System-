# Modern Inventory Tracking System

## Overview

This project is a **Modern Inventory Tracking System** built using Python and the Tkinter library. It allows users to manage an inventory of products, including adding, editing, deleting, searching, and saving product records to a CSV file.

## Features

1. **Add Products**: Add new products to the inventory.
2. **Edit Products**: Update details of existing products.
3. **Delete Products**: Remove products from the inventory.
4. **Search Products**: Search for products by name.
5. **Save Inventory**: Save the inventory records to a CSV file.
6. **Restore Inventory**: Load inventory records from a CSV file.

## Requirements

- Python 3.x
- Tkinter (built-in with Python)
- `csv` module (built-in with Python)
- `os` module (built-in with Python)

## File Structure

- `InventoryApp`: The main class handling the application logic.
- `Product`: A class representing a product entity.
- `Inventory.csv`: A file used to store the inventory records.

## Setup Instructions

1. Make sure you have Python 3 installed.
2. Save the script to a file (e.g., `inventory_management.py`).
3. Run the script using the following command:
   ```bash
   python inventory_management.py
   ```

## Usage

### Add a Product

1. Click on the **ADD Item** button.
2. Enter the product details (Name, Price, Quantity) in the popup window.
3. Click the **ADD** button to save the product.

### Edit a Product

1. Select a product from the table.
2. Click on the **Edit Product** button.
3. Update the product details in the popup window.
4. Click the **Update** button to save the changes.

### Delete a Product

1. Select a product from the table.
2. Click on the **Delete Product** button.
3. Confirm the deletion in the popup dialog.

### Search for a Product

1. Enter a search term (product name) in the search bar.
2. Click the **Search** button to filter the results.
3. To clear the search, click the **Clear Search** button.

### Save the Inventory

- Click on the **Save Inventory** button to save the inventory to the `Inventory.csv` file.

### Restore Inventory

- Click on the **Show Inventory** button to reload records from the `Inventory.csv` file.

## Code Structure

### Classes

#### 1. `Product`

- Represents a product with the following attributes:
  - `name` (str): Name of the product.
  - `price` (float): Price of the product.
  - `quantity` (int): Quantity of the product.

#### 2. `InventoryApp`

- Inherits from `Product` and handles the application logic.

### Key Functions

1. **`add_item()`**: Adds a new product to the inventory and saves it to the CSV file.
2. **`edit_product()`**: Edits the details of a selected product.
3. **`delete_product()`**: Deletes a selected product and updates the CSV file.
4. **`search_product()`**: Searches for products matching a query.
5. **`clear_search()`**: Clears the search and restores all products.
6. **`save_inventory()`**: Saves the inventory to a CSV file.
7. **`restore_inventory()`**: Loads products from the CSV file.

### CSV Operations

- **`save_inventory_in_csv()`**: Appends a new product to `Inventory.csv`.
- **`update_inventory_in_csv()`**: Updates the `Inventory.csv` file with the current inventory state.

## Example CSV Format

```csv
Name,Price,Quantity
Laptop,800.00,10
Mouse,20.00,50
Keyboard,30.00,30
```

## Acknowledgments

- **Tkinter**: For providing the GUI functionality.
- **CSV Module**: For managing inventory data storage.
- **OS Module**: For file operations.

