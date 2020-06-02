# NAME : INSTAGRAM

## DESCRIPTION 
.Instragram is an application that enables users to post their post and can be followed by other users.Their post can be shared ,commented and liked others.


## AUTHOR
BIRON OTIENO ODHIAMBO

## CLONE
Fork this repository or clone it to your local machine on ubuntu use the following commands

git clone this repo https://github.com/Biphyl/instagram

## USER STORY
As a user of the application you will be able to:

1 View different posts from accounts followed
2 Click on a single photo to expand it and also view the details of the photo.
3 Search for user profiles
comment on photos
4 Like posts
5 Upload Posts with caption
6 Follow other users


## INSTALLATION
1.set up a virtual environment using the following command.

python3 -m venv  venv
And activate virtual

source virtual/bin/activate

2.Install the requirements use the command.
pip install -r requirements.txt

3.create a .env file and add

SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'

4.create a database using postgres

CREATE DATABASE <your-database-name>

5.create a migration using the following command
python3 manage.py makemigrations

migrate

python3.6 manage.py migrate

6.create a super user for admin account
python 3.6 manage.py createsuperuser
add your password and username , email is not a must.

7.To run user :
python3 manage.py runserver

navigate to admin by adding /admin to your local host url like so :

127.0.0.1:8000/admin

## TECHNOLOGIES USED
1:Html5 and Css3
2:Python
3:Bootstrap 3
4:Django

## LICENSE
This project is licensed under the [MIT] license
