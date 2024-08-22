# Expense tracker api

The Expense Tracker API is a RESTful service designed to manage personal finances by allowing users to track their income, expenses, and savings. It offers a robust set of endpoints to add, update, delete, and view financial transactions. Users can categorize their expenses (e.g., groceries, rent, entertainment) and visualize their spending patterns over time.

## Set up

Clone the repository

```bash
git clone "https://github.com/hanzeelvilla/expense-tracker-api.git"
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment 

Command for windows

```bash
.\.venv\Scripts\Activate.ps1
```

Command for linux
```bash
source .venv/bin/activate
```

Install the requirements

```bash
pip install -r requirements.txt
```

Create a .env file and a SECRET_KEY

You can run this comand that generates a a functional SECRET_KEY

```python
python -c "import secrets; print(secrets.token_urlsafe())"
```


Create the database

```python
python manage.py migrate
```

Create a superuser

```python
python manage.py createsuperuser
```

If you want to, you can run the following command to fill the db with some test data

```python
python.exe .\manage.py  fill_with_test_data
```

Run the server

```python
python.exe .\manage.py runserver
```

If you fill the db with the test data you can try it out with the commands in the .rest files, you will need the extension REST CLIENT from visual studio code. 

1. First you need to run the .rest file (clicking in each endpoint) in the authorization app so you can get you token.
2. Then copy and paste it inside the TOKEN variable in the .rest file inside expenses app.

## FEATURES
- User Authentication
- Category Management
- Date-based Sorting and Filtering