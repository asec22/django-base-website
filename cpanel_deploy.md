# cPanel Deployment

## Deployment in cPanel using a .zip file

1. Once you have made your adjustments in VS Code, or whatever you code editor you use, please zip the djangobaseproject directory on your computer.

2. Login to cPanel and navigate to the File Manager under Tools >> Files. Go to your home directory and upload the .zip file to home directory.  Extract the contents and move the style.css file to your public_html directory static folder.  If no static folder exists, create one.  

3. Navigate to Tools >> Software >> Setup Python App. Create a New Application.  Fill in the directory, an url for the app, and the log file and select the version of Python.  Leave the rest blank and click Create.  You can confirm its creation by opening the page using the arrow next the url input on the creation page. 

4. Once confirmed, go to the settings.py under djangoproject folder and enter the url for your website in the ALLOWED_HOSTS and enter the static file url for the style.css in the base.html under the basewebbapp.  You may also need adjust the links for the home, about, services, and contact pages in base.html based on your inputs into the url on the Python App creation page.

5. Now click on the virtual environment command that now exists on the top of the creation page to copy the command. Navigate to the Tools >> Advanced >> Terminal.  You may have to create SSH access to have access to the Terminal in cPanel. Once in the Terminal, past the command to activate the virtual enviroment.  Once in the enviroment, enter ```pip install -r requirements.txt``` to install django, whitenoise, crispy_forms, and crispy_bootstrap5.

6. Enter ```python manage.py makemigrations``` and ```python manage.py migrate``` to create the databases needed.

7. Navigate under the File Manager  to djangobaseproject and select the file and click on edit the passenger-wgsi.py file. Edit the file by commenting out the definition and entering:
  
```python
import os
import sys



#sys.path.insert(0, os.path.dirname(__file__))


#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    message = 'It works!\n'
#    version = 'Python %s\n' % sys.version.split()[0]
#    response = '\n'.join([message, version])
#    return [response.encode()]

from djangobaseproject.wsgi import application

```
This will call your application from the wsgi.py file under djangobaseproject. 

8. Navigate back to the creation page under Setup App by clicking the pencil icon next the app link.  Click on Restart. Now everything should be set and you should see your page up and running.

Here is an example of the app running in cPanel: [https://app.lifespectralsurvey.com/djangobaseproject/home/](https://app.lifespectralsurvey.com/djangobaseproject/home/). I consulted this video for the procedure: [https://youtu.be/h2w8oNw_W80?si=w3GXcbp8zuX10QZn](https://youtu.be/h2w8oNw_W80?si=w3GXcbp8zuX10QZn).

