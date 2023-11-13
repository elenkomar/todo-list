**todo-list**
---------------------
Django project for managing tags and tasks in Todo-list.

**Check-out**
--------------------



**Setup**
-------------------
1. Clone the project:
* git clone https://github.com/elenkomar/Restaurant_Kitchen_Service.git

2. Create virtual environment and activate it
for Windows

* python -m venv venv

* venv\Scripts\activate

3. Install dependencies
* pip install -r requirements.txt

4. Run migrations
* python manage.py migrate

5. Create superuser
* python manage.py createsuperuser (enter your username and password)

6. Run server on local host

* you must create .env file with your data (look at exemple in .env.sample)

* python manage.py runserver

**Demo**
--------------------
![creat_task.jpg](screenshot_pages%2Fcreat_task.jpg)
![create_tag.jpg](screenshot_pages%2Fcreate_tag.jpg)
![home_page.jpg](screenshot_pages%2Fhome_page.jpg)
![tags.jpg](screenshot_pages%2Ftags.jpg)