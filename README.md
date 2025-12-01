# ohtuvarasto

A simple warehouse management application built with Python.

## Features

- Create and manage multiple warehouses
- View warehouse capacity, balance, and available space
- Add items to warehouses
- Take items from warehouses
- Delete warehouses
- Web-based user interface using Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Roope2003/ohtuvarasto.git
   cd ohtuvarasto
   ```

2. Install dependencies:
   ```bash
   pip install flask pytest pylint
   ```

## Running the Web Application

Start the Flask web server:

```bash
cd src
python -m flask --app app run
```

Or run directly:

```bash
cd src
python app.py
```

The application will be available at `http://localhost:5000`.

## Web UI Usage

1. **Home Page**: View all created warehouses with their current status
2. **Create Warehouse**: Click "Create New Warehouse" to add a new warehouse with a name, capacity, and optional initial balance
3. **View Warehouse**: Click on a warehouse to see detailed information and perform operations
4. **Add Items**: Enter an amount and click "Add to Warehouse" to add items
5. **Take Items**: Enter an amount and click "Take from Warehouse" to remove items
6. **Delete Warehouse**: Use the "Delete Warehouse" button to remove a warehouse

## Running Tests

```bash
cd src
python -m pytest tests/ -v
```

## Project Structure

```
src/
├── app.py              # Flask web application
├── varasto.py          # Warehouse (Varasto) class
├── index.py            # Example console application
├── templates/          # HTML templates
│   ├── base.html       # Base template with styling
│   ├── index.html      # Home page
│   ├── create.html     # Create warehouse form
│   └── warehouse.html  # Warehouse detail view
└── tests/
    └── varasto_test.py # Unit tests
```