# Passport Queue - [Django Pixel Lite](https://appseed.us/django/django-pixel-bootstrap-uikit)

Open-Source **[Django](https://appseed.us/django)** starter coded with basic modules, database, ORM and deployment scripts on top of **[Pixel Lite](https://docs.appseed.us/content/bootstrap-template/pixel-lite-template)** UI Kit, a fully responsive and modern **Bootstrap 5 UI Kit** that will help you build creative and professional websites. The Django codebase is provided with database, ORM, authentication, and deployment scripts. 

<br />

> Links

- 👉 [Django Pixel Lite](https://appseed.us/django/django-pixel-bootstrap-uikit) - product page
- 👉 [Django Pixel Lite](https://django-pixel-lite.appseed-srv1.com/) - LIVE Deployment
- 👉 More [Django Apps](https://appseed.us/django) - provided by AppSeed 

<br />

## ✨ How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-pixel.git
$ cd django-pixel
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
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
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Passport Registration
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

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## ✨ Deployment

I am deploying this app through CPanel hosting with GoDaddy and using a MySQL database in the same place. I will update how to with this later. Maybe even a local deployment option as well.

Switching the DB Location is shown in the Core\Settings.py file

<br />

## ✨ Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Django Pixel Lite](https://appseed.us/django/django-pixel-bootstrap-uikit) - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
