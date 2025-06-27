import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load inventory data
def load_inventory():
    file_path = 'inventory.json'
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

# Save inventory data
def save_inventory(data):
    with open('inventory.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Home
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# Inventory page
@app.route('/inventory')
def inventory():
    inventory_data = load_inventory()
    return render_template('inventory.html', inventory=inventory_data)

# Add Item
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        price = float(request.form.get('price'))
        stock = int(request.form.get('stock'))

        inventory = load_inventory()
        item_id = inventory[-1]['item_id'] + 1 if inventory else 1

        new_item = {
            'item_id': item_id,
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
        }

        inventory.append(new_item)
        save_inventory(inventory)
        return redirect(url_for('inventory'))

    return render_template('add_item.html')

# Sales page
@app.route('/sales', methods=['GET', 'POST'])
def sales():
    inventory = load_inventory()

    if request.method == 'POST':
        item_id = int(request.form.get('item_id'))
        quantity = int(request.form.get('quantity'))

        for item in inventory:
            if item['item_id'] == item_id:
                if item['stock'] >= quantity:
                    item['stock'] -= quantity
                else:
                    return "Error: Not enough stock."

        save_inventory(inventory)
        return redirect(url_for('inventory'))

    return render_template('sales.html', inventory=inventory)

@app.route('/dashboard')
def dashboard():
    inventory = load_inventory()
    print("Inventory Data:", inventory)
    return render_template('dashboard.html', inventory=inventory)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
