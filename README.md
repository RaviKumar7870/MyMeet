Hello!

Welcome to MyMeet WebApp

I have used Django stack for this Webapp. The Purpose of this webapp is to reduce the load of students by allowing them to keep their all class link in our WebApp. In this Webapp one can simply login with their credential and store the class link here.

Soon We are going to implement Email Feature. By this user will get email as remainder just before the class start



App Link - mymeetapp.herokuapp.com

Run this Repository on your Local Machine :

First fork this repo and then Clone it
Run cd MyMeet - to move into the directory
Install virtualenv using command - pip install virtualenv
Now activate the virtual environment using command - virtualenv env
Now activate the virtual env using command - .\env\Scripts\activate . This will activate the virtual environment. For linux and Mac try - source env/bin/activate
Install all requirements by - pip install -r requirements.txt.
Now to migrate the models run - python manage.py migrate.
Now to activate the localhost server run - python manage.py runserver
Now open localhost:8000 on your browser
