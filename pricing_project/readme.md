# Pricing Module

This is a Django web application that provides a configurable pricing module.

## Prerequisites
- Python 3.x
- Django 3.x

## Installation
1. Clone the repository: `git clone https://github.com/kunal015/Fynd.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Apply database migrations: `python manage.py migrate`

## Usage
1. Run the development server: `python manage.py runserver`
2. Log in with superuser credentials or create a new superuser using `python manage.py createsuperuser`
3. Access the Django Admin interface at `http://localhost:8000/admin/`
4. Use the custom admin form to add, modify, and remove pricing configurations.
5. To calculate pricing using the API, make a GET request to `http://localhost:8000/api/calculate_pricing/` with parameters `distance`, `time`.
A sample json body is mentioned below:- 
{
  "distance": "5.00",
  "time": "1.25"
}

## Tests (Optional)
Run the tests using the following command:
```bash
python manage.py test