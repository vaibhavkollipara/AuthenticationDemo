# AuthenticationDemo
Django web app to implement authentication mechanisms with email verification

## Technologies
* Python 3
* Django 1.10
* Jinja 2
* Django Forms
* SQLite db
* HTML
* CSS
* Bootstrap

### Instructions
Environment Setup
* `cd AuthenticationDemo`
* `pip install -r requirements.txt`
* `python manage.py migrate`

Add email details
* Add your gmail account credentials in settings.py file
* Enable your gmail account to connect to less secure apps. <a href="https://support.google.com/accounts/answer/6010255?hl=en">Instructions</a>

Create Admin account
* `python manage.py createsuperuser`

Run Server
* `python manage.py runserver`

### Screenshots
<img style="border:2px solid black;" src="https://github.com/vaibhavkollipara/AuthenticationDemo/blob/master/screens/login.PNG?raw=true"/><br/>
<img style="border:2px solid black;" src="https://github.com/vaibhavkollipara/AuthenticationDemo/blob/master/screens/profile.PNG?raw=true"/><br/>
