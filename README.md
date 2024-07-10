# Django Base Website

## A repository for a base website written for the Django architecture.

Django Base Website is a respository that is written in the Django pyton architecture.  The base website allows for quick deployment for a website on any platform (Azure, Google Cloud, cPanel shared). Four basic HTML pages (home, about, services, and contact) are included here which extend a base HTML page in jinja architecture. The pages can be modified and copied for extra information. 

## Instructions on how to the test the website in the local environment in a localhost:

1. You have already done the first step by cloning this project into a nice, clean, empty folder.  Also make sure you have entered your python directory into the enviroment variable PATH in your computer to acces python from any directory. 

2. Change to the new folder, but not the cloned directory, and type this command into a terminal: ```python -m venv \path_to_your_forlder\.venv```. This will create the virtual environment with python installed locally into your folder. You can do this in any terminal in any program that supports the terminal on your computer.

3. Enter ```.venv\scripts\activate``` to activate the environment.

4. Enter the django-base-website/djangobaseproject directory. Type ```pip install -r requirements.txt``` to install django, django-crispy-forms, and crispy-bootstrap5. Bootstrap 5 and Font Awsome styling are already installed in the base.html.  You can go to [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) and [Font Awsome](https://fontawesome.com/) for more information. You can style the pages using the styles.css file in the static folder.  Also, you may remove any styling you wish.

5. To create the admin database in SQLlite for this project, enter ```python manage.py makemigrations```. Once the manager sets up the buid parameters, type ```python manage.py migrate``` to complete the migrations to the database.  Right now only the admin databases plus the contact model for the contacts from the contact.html page.

6. In order for the contatct form on contact.html to work, you must set the SMTP settings in djangobaseproject folder's settings.py file.  The settings are at the bottom of the settings.py file.  You will need to see your emails website docementation on SMTP on their settings and activate SMTP with your email host provider. You will need to also enter the correct emails into the views.py file under basewebapp folder to direct the mail.  The documentation in the file will indicate where to enter which email address.

7. We are almost at the testing stage, just type ```python manage.py runserver``` to run the virtual server on your computer. Click on the link in the terminal to open the site, it should display the home page if everything worked out.

## The flow of directories should be:

Created Directory --> .venv,django-base-website --> djangobaseproject --> djangobaseproject,basewebapp

You can add apps to the base project by using ```python manage.py startapp mynewapp``` and name it anything you wish.  You can deploy this on Azure, cPanel, or Google Cloud as per their app registries.

Here are two guides for deployment:
1. [Azure Guide](azure_deploy_vscode_guide.md)
2. [cPanel Guide](cpanel_deploy.md)

Hope you have fun in testing and expanding on this base website! 🙂


    
   
