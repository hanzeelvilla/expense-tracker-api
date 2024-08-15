# Expense tracker api

The Expense Tracker API is a RESTful service designed to manage personal finances by allowing users to track their income, expenses, and savings. It offers a robust set of endpoints to add, update, delete, and view financial transactions. Users can categorize their expenses (e.g., groceries, rent, entertainment) and visualize their spending patterns over time.

## Set up

Clone the repository

```bash
git clone "https://github.com/hanzeelvilla/simple-ecommerce.git"
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

```bash
.\.venv\Scripts\Activate.ps1
```

Install the requirements

```bash
pip install -r requirements.txt
```

Create the database

```python
python manage.py migrate
```

Create a superuser

```python
python manage.py createsuperuser
```

Run the server
```python
python.exe .\manage.py runserver 
```