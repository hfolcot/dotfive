django
sqlite db
crispy forms

django channels can be used for websockets - not familiar enough at this stage

# Category Manager
### Heather Olcot
An application to manage different items in categories and subcategories of infinite depth.

## User Stories (from project brief)
Mark wants to keep track of his belongings. He logs in, and is presented with a list of
categories, showing the different levels visually. He adds “Electronics”, and under that,
“Televisions”. To this category he adds the items “49-inch LCD”, “40-inch plasma”, and
“32-inch CRT”.
Sandy logs in and creates “Gaming consoles”, and under this, the items “PS4 Pro”, “XBox
One X”, and “Nintendo Switch”.
Mark sees Sandy’s entries appear. He edits “Gaming consoles” to sit under “Electronics”.
This change appears on Sandy’s screen as soon as he has done it.


## Features
The app has login functionality; multiple users can log in and use the software at the same time.
Users can add and edit categories and place them under parent categories.


### Features Left to Implement
Users are currently unable to see each others' changes without refreshing. This functionality can be built into the app using the Django Channels package to set up websockets; unfortunately I have no previous experience with web sockets or Django channels and will need to implement this when I have been able to spend some time doing solid research on this.

## Technologies Used
The application is written in Python using the Django framework and uses HTML and CSS for the UI. Javascript is also used to enhance the user experience and this is supported with the JQuery library.
The Bootstrap CSS framework has been used for responsiveness and other styling, along with FontAwesome icons. The Django Crispy Forms package has also been installed for form styling.
The Django Rest Framework has also been used to implement an API. This is used to retrieve data from the database after the page has already loaded.
The database uses SQLite.


## Testing
Some automated unit tests have been written; these files can be found in the categories folder and names are all prefixed with `test_`.
The display has been tested at all screen widths down to 520px.

## Deployment
#### These are instructions for deploying the application in a development environment
1. Unzip the files to a folder of your choice.
2. Navigate to this folder in your CLI.
3. Set up a virtual environment if desired and activate.
4. Run `pip install -r requirements.txt` to install dependencies.
5. Rename `env.sample.py` to `env.py` and update the values according to your local environment (at this stage only the secret key is a required environment variable)
6. Run `python manage.py makemigrations` and then `python manage.py migrate` to create the database.
7. Run `python manage.py createsuperuser` and enter new credentials. This will set up your admin account.
8. Run `python manage.py runserver'.
9. The application will be running at `127.0.0.1:8000`. Please note if you are running the application anywhere else you will need to add the address to ALLOWED_HOSTS in the settings.py file under the categoryManager folder.
10. Admin functionality can be found at /admin.