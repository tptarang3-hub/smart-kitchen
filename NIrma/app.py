from flask import Flask, jsonify, render_template, request, send_from_directory
import db_handler

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def serve_homepage():
    return render_template('index.html')

@app.route('/another_page.html')
def serve_another_page():
    return render_template('another_page.html')

@app.route('/index1.html')
def serve_index1():
    return render_template('index1.html')

@app.route('/waste_monitoring.html')
def serve_waste_monitoring():
    return render_template('waste_monitoring.html')
@app.route('/analytics.html')
def serve_analytics():
    return render_template('analytics.html')

@app.route('/App.css')
def serve_css():
    return send_from_directory(app.static_folder, 'App.css')

@app.route('/styles.css')
def serve_styles():
    return send_from_directory(app.static_folder, 'styles.css')

@app.route("/inventory", methods=["GET"])
def get_inventory():
    inventory = db_handler.get_inventory()
    return jsonify(inventory)

@app.route("/recipe", methods=["GET"])
def suggest_recipe():
    recipe = db_handler.get_recipe()
    return jsonify({"recipe": recipe})

@app.route('/add_item', methods=['POST'])
def add_item():
    required_fields = ['item_name', 'quantity', 'expiry_date', 'category']
    if not all(field in request.form for field in required_fields):
        return jsonify({"message": "All fields are required!"}), 400

    item_name = request.form['item_name']
    quantity = request.form['quantity']
    expiry_date = request.form['expiry_date']
    category = request.form['category']
    db_handler.add_item(item_name, quantity, expiry_date, category)
    return jsonify({"message": "Item added successfully!"})

@app.route('/update_item', methods=['POST'])
def update_item():
    required_fields = ['item_id', 'item_name', 'quantity', 'expiry_date', 'category']
    if not all(field in request.form for field in required_fields):
        return jsonify({"message": "All fields are required!"}), 400

    item_id = request.form['item_id']
    item_name = request.form['item_name']
    quantity = request.form['quantity']
    expiry_date = request.form['expiry_date']
    category = request.form['category']
    db_handler.update_item(item_id, item_name, quantity, expiry_date, category)
    return jsonify({"message": "Item updated successfully!"})

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
