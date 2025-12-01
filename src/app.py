"""Flask web application for the ohtuvarasto warehouse."""

from flask import Flask, render_template, request, redirect, url_for, flash
from varasto import Varasto

app = Flask(__name__)
app.secret_key = 'ohtuvarasto-secret-key'

# Global warehouse instances dictionary to manage multiple warehouses
warehouses = {}


@app.route('/')
def index():
    """Display the main page with all warehouses."""
    return render_template('index.html', warehouses=warehouses)


@app.route('/create', methods=['GET', 'POST'])
def create_warehouse():
    """Create a new warehouse."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        try:
            capacity = float(request.form.get('capacity', 0))
            initial_balance = float(request.form.get('initial_balance', 0))
        except ValueError:
            flash('Invalid capacity or initial balance. Please enter numbers.', 'error')
            return render_template('create.html')

        if not name:
            flash('Warehouse name is required.', 'error')
            return render_template('create.html')

        if name in warehouses:
            flash(f'Warehouse "{name}" already exists.', 'error')
            return render_template('create.html')

        warehouses[name] = Varasto(capacity, initial_balance)
        flash(f'Warehouse "{name}" created successfully.', 'success')
        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/warehouse/<name>')
def view_warehouse(name):
    """View a specific warehouse."""
    if name not in warehouses:
        flash(f'Warehouse "{name}" not found.', 'error')
        return redirect(url_for('index'))

    warehouse = warehouses[name]
    return render_template('warehouse.html', name=name, warehouse=warehouse)


@app.route('/warehouse/<name>/add', methods=['POST'])
def add_to_warehouse(name):
    """Add items to a warehouse."""
    if name not in warehouses:
        flash(f'Warehouse "{name}" not found.', 'error')
        return redirect(url_for('index'))

    try:
        amount = float(request.form.get('amount', 0))
    except ValueError:
        flash('Invalid amount. Please enter a number.', 'error')
        return redirect(url_for('view_warehouse', name=name))

    warehouse = warehouses[name]
    warehouse.lisaa_varastoon(amount)
    flash(f'Added {amount} units to "{name}".', 'success')
    return redirect(url_for('view_warehouse', name=name))


@app.route('/warehouse/<name>/take', methods=['POST'])
def take_from_warehouse(name):
    """Take items from a warehouse."""
    if name not in warehouses:
        flash(f'Warehouse "{name}" not found.', 'error')
        return redirect(url_for('index'))

    try:
        amount = float(request.form.get('amount', 0))
    except ValueError:
        flash('Invalid amount. Please enter a number.', 'error')
        return redirect(url_for('view_warehouse', name=name))

    warehouse = warehouses[name]
    taken = warehouse.ota_varastosta(amount)
    flash(f'Took {taken} units from "{name}".', 'success')
    return redirect(url_for('view_warehouse', name=name))


@app.route('/warehouse/<name>/delete', methods=['POST'])
def delete_warehouse(name):
    """Delete a warehouse."""
    if name not in warehouses:
        flash(f'Warehouse "{name}" not found.', 'error')
        return redirect(url_for('index'))

    del warehouses[name]
    flash(f'Warehouse "{name}" deleted successfully.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
