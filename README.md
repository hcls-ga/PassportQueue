# Passport Queue - [Django Pixel Lite](https://appseed.us/django/django-pixel-bootstrap-uikit)

Open-Source **[Django](https://appseed.us/django)** starter coded with basic modules, database, ORM and deployment scripts on top of **[Pixel Lite](https://docs.appseed.us/content/bootstrap-template/pixel-lite-template)** UI Kit, a fully responsive and modern **Bootstrap 5 UI Kit** that will help you build creative and professional websites. The Django codebase is provided with database, ORM, authentication, and deployment scripts. 

<br />

> Links

- 👉 [Django Pixel Lite](https://appseed.us/django/django-pixel-bootstrap-uikit) - product page
- 👉 [Django Pixel Lite](https://django-pixel-lite.appseed-srv1.com/) - LIVE Deployment
- 👉 More [Django Apps](https://appseed.us/django) - provided by AppSeed 
- 👉 [Deploying This App Onto CPanel](https://medium.com/@pyzimos/deploying-django-web-application-using-cpanel-6687b8057439)
<br />

## ✨ How to use it

```bash
$ # Get the code
$ git clone https://github.com/hcls-ga/PassportQueue.git
$ cd PassportQueue
$
$ # Start Conda and Activate Environment
$ C:/ProgramData/Anaconda3/Scripts/activate.bat
$ conda activate django #The Environment made for this is named 'django'
$
$ # Install modules - SQLite Storage
$ # pip install -r requirements.txt
$ pip3 install -r requirements.txt
$
$ # Create Admin Account for Staff Login
$ python manage.py create superuser
$ Username: admin
$ Email Address: admin@example.com
$ Password: *********
$ Password (again): *********
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |    |-- model.py                  # Defines the model for a Patron
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- includes.old/             # Test Templates
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page (Disabled)
   |         |
   |         |-- admin/
   |         |    |--index.html             # Admin Backend
   |         |    |--base.html              # Standard Edit Screen
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Passport Registration
   |              |-- index_es.html         # Passport Registration in Spanish
   |              |-- index_kn.html         # Passport Registration in Korean (Not Completed)
   |              |-- sucess.html           # Sucess Page
   |              |-- sucess_es.html        # Sucess Page in Spanish
   |              |-- sucess_kn.html        # Sucess Page in Korean (Not Completed)
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## ✨ Deployment

I am deploying this app through CPanel hosting with GoDaddy and using a MySQL database in the same place. I will update how to with this later. Maybe even a local deployment option as well.
- 👉 [Deploying This App Onto CPanel](https://medium.com/@pyzimos/deploying-django-web-application-using-cpanel-6687b8057439)

## ✨ Testing Locally

In order to test locally vs running in CPanel, you must change the secret key and th DB Location as shown in the Core\Settings.py file

:heavy_exclamation_mark: <b> IMPORTANT <b/> :heavy_exclamation_mark:
<br />
You need to remove these changes prior to commiting to repo and DEFINITELY before making a pull request


### Changing the Secrect Code Location
```python
18 # Grab Stuff from Secrets.json
19 
20 with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
21     secrets = json.load(secrets_file)
22
23 def get_secret(setting, secrets=secrets):
24     #Get secret setting or fail with ImproperlyConfigured
25     try:
26         return secrets[setting]
27     except KeyError:
28         raise ImproperlyConfigured("Set the {} setting".format(setting))
30 
31
32 # SECURITY WARNING: keep the secret key used in production secret!
33 SECRET_KEY = get_secret('SECRET_KEY')
34 """
35 #This is the security key for non-live versions
36 SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')
37 """ # Move these quotes
```
```python
18 # Grab Stuff from Secrets.json
19 """ # To this location
20 with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
21     secrets = json.load(secrets_file)
22
23 def get_secret(setting, secrets=secrets):
24     #Get secret setting or fail with ImproperlyConfigured
25     try:
26         return secrets[setting]
27     except KeyError:
28         raise ImproperlyConfigured("Set the {} setting".format(setting))
30 
31
32 # SECURITY WARNING: keep the secret key used in production secret!
33 SECRET_KEY = get_secret('SECRET_KEY')
34 """
35 #This is the security key for non-live versions
36 SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')
37 
```
<br />

### Changing the Location of the Database and DB Engine

<br />

```python
 92 # Database
 93 # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
 94
 95 # Use this for test environments
 96 
 97 DATABASES = {
 98     'default': {
 99         'ENGINE' : 'django.db.backends.mysql',
100         'NAME' : 'beta-hclsPassport',
101         'USER': 'betahclsPassport',
102         'PASSWORD': get_secret('DB_PASSWORD'),
103         'HOST': '127.0.0.1',
104     }
105 }
106 """
107 DATABASES = {
108     'default': {
109         'ENGINE': 'django.db.backends.sqlite3',
110         'NAME': 'db.sqlite3',
111     }
112 }
113 """ # Move these quotes to
```
```python
 92 # Database
 93 # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
 94
 95 # Use this for test environments
 96 """ # To this location
 97 DATABASES = {
 98     'default': {
 99         'ENGINE' : 'django.db.backends.mysql',
100         'NAME' : 'beta-hclsPassport',
101         'USER': 'betahclsPassport',
102         'PASSWORD': get_secret('DB_PASSWORD'),
103         'HOST': '127.0.0.1',
104     }
105 }
106 """
107 DATABASES = {
108     'default': {
109         'ENGINE': 'django.db.backends.sqlite3',
110         'NAME': 'db.sqlite3',
111     }
112 }
113 
```
<br />

## ✨ Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github
- [Dylan Young](Hallcountylibrary.org) - Hall County Library
<br />

---
