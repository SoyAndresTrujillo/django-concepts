# 2024-10-23

## Install virtual enviroment 🤯
```bash
python3 -m venv ~/.envs/my-frist-env
```
Check if the virtual environment is installed
```bash
ls ~/.envs
```
## Activate virtual enviroment 🤯
```bash
source ~/.envs/my-frist-env/bin/activate
```
Now we can execute the python command
## Install Django
```bash
pip install Django
```
## Show commands
```bash
django-admin --help
```
## Create a new project
```bash
django-admin startproject my_first_project
```
note: the project name must be in lowercase and use underscore instead of dash
## Show commands for manage the project
```bash
python manage.py --help
```
## Run the server
```bash
python manage.py runserver
```
# Create new app into the project my_first_project file
```bash
python manage.py startapp my_first_app
```
## Generate migrations
```bash
python manage.py makemigrations
```
## Do migrations
```bash
python manage.py migrate
```
## Show bd
```bash
python manage.py dbshell
```
Show tables
```bash
.tables
```
Show schema
```bash
.schema name_table
```
example:
```bash
sqlite> .tables
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups            my_first_app_car          
auth_user_user_permissions
sqlite> .schema my_first_app_car 
CREATE TABLE IF NOT EXISTS "my_first_app_car" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" text NOT NULL, "year" text NULL, "color" text NULL);
sqlite> SELECT * FROM my_first_app_car;
1|BMW|2023|
2|BMW|2023|Black
sqlite> SELECT * FROM my_first_app_car where id=1;
1|BMW|2023|
sqlite> SELECT * FROM my_first_app_car where id=2;
2|BMW|2023|Black
```
## Entry our python shell
```bash
python manage.py shell
```
example:
```bash
>>> from my_first_app.models import Car
>>> my_car = Car(title="BMW", year="2023", color="Black")
>>> print(my_car)
BMW - 2023 - Black
>>> my_car.save()
```
## Install interactive shell for auto complete and more features
```bash
pip install ipython
```
