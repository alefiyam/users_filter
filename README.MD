Configuration details for this application
------------------------------------------

To configure this appliction into your local machine you must have installed python and pip package of python.

Once you have installed above requirements then follow these instruction to configure this application.

clone/download this application repository into your local machine.
then navigate to users_filter_app directory and execute the following commands

In users_filter_app directory , execute the command
    
    pip install -r requirements.txt

this will install all require application dependencies.
As we used the MySql database , set the username , password , database name
in settings.py and then execute the command 

    python manage.py makemigrations
    python manage.py migrate 

To start this application just run the following command

    python manage.py runserver

Create a Admin/Superuser by command 

    python manage.py createsuperuser

Then to create recruiters go the the admin panel using url

	http://localhost:8000/admin/
    To access the admin panel give login credentials of admin
    then create recruiters in Users Table
    create employes with their resume details in Employees Table


You can access the application on your browser using this url.

	http://localhost:8000/login
	Give the login credentials and then it will redirect to the url:
	http://localhost:8000/search


Following actions should be done:

	
1. Filter Page: Goto search page to see the user profiles by applying filters ,
                enter the location , skills , experience etc in textbox , then click
                on search button to see the filtered profiles.   
	
	http://localhost:8000/search

2. Create CSV File: To generate the csv file of the filtered table , click the link 
                    "Export Table data into CSV", below the table , it will generate
                    the csv file.	


		
