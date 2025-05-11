===============================================
Kodhami Django Project - Setup Guide
===============================================

1. SET UP VIRTUAL ENVIRONMENT
-----------------------------
Open terminal/command prompt in the project folder (where manage.py is located):

For Windows:
> pipenv shell

For Mac/Linux:
$ python3 -m venv venv
$ source venv/bin/activate

2. INSTALL DEPENDENCIES
-----------------------
With virtual environment activated:

> pip install -r requirements.txt

If requirements.txt doesn't exist:
> pip install pipenv
> pipenv install

5. SET UP DATABASE
------------------
- Install MySQL Workbench (or your preferred database)
- Create a database named 'kodhami' (or your preferred name)
- Update database settings in kodhami/settings.py:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'kodhami',
          'USER': 'your_username',
          'PASSWORD': 'your_password',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }

6. RUN MIGRATIONS
-----------------
> python manage.py migrate

7. CREATE SUPERUSER (Optional)
------------------------------
> python manage.py createsuperuser
Follow prompts to create admin account

8. RUN DEVELOPMENT SERVER
-------------------------
> python manage.py runserver

9. ACCESS THE PROJECT
---------------------
- Open browser and go to: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

10. PROJECT STRUCTURE
---------------------
- kodhami/       : Main project settings
- users/         : User authentication app
- templates/     : HTML templates
- static/        : CSS, JS, images
- manage.py      : Django management script