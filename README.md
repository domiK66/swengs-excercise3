# Lab exercise 3
We develop a simple movie site called "movie_site" (the Django 
project) that uses a Django app called "yamod" (yet another 
movie databases)

• The project "movie_site" holds all necessary configuration for 
your site. 

• The Django app "yamod" will contain database tables, API 
endpoints and tests
# Setup
1. Create a virtual environment (called swengs21)

2. Activate the virtual environment

3. Install Django: 
```bash
C:\> pip install django
```
4. Create a project directory project (including a subfolder apps)

5. Create a django project called "movie_site" in your project folder Creating a Django project 
```bash
C:\project> django-admin startproject movie_site
```
6. Initializing your project:
```bash
C:\project\movie_site> python manage.py migrate
```
```bash
C:\project\movie_site> python manage.py createsuperuser
```
user: kainzdom19 / 
password: admin

```bash
C:\project\movie_site> python manage.py runserver
```

7. Download and unzip the yamod app into the apps folder

8. Open a shell and navigate to the yamod folder – you should see a setup.py file

9. Run pip install -e . in the yamod folder

10. Add yamod to INSTALLED_APPS in settings.py

11. Run python manage.py migrate (this will add yamod's database tables)
```bash
C:\project\movie_site> python manage.py migrate
```

12. Try running the application server, open the Django admin app to see if everything is working

# Implement Tests
1. Open yamod/tests.py and implement the test methods testing insert/update/deletes on the yamod models

2. run python manage.py test yamod in your movie_site project to see, if your tests work
```bash
C:\project\movie_site> python manage.py test yamod
```


Finally if there is time: adjust admin.py and include models in the Django admin app