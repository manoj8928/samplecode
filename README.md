First Time Setup

Install virtualenv and activate

virtualenv venv && source venv/bin/activate

pip install -r requirements.txt

Install postgres and locally'.

Look into config folder for the env vars to be set.

You could use config/__init__.py as an example to create database, schema, and user.

Then:
python manage.py db upgrade

Run Test Cases
python -m nose --nocapture --cover-package=api  -v  tests/

Start development server, navigate to url

python manage.py runserver