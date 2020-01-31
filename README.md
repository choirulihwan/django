# django
list of django based app:
1. Real estate App (python 3.7, mysql, django3.0)

# step by step django
- installl python
- install pycharm
- setting venv and interpreter
- install django
- create project django : 
- start server 	: python manage.py runserver

# create template in django
- create dir templates in <project>
- set 'DIRS': [os.path.join(BASE_DIR, 'templates')] in <project>/settings.py

# manage static files in django
- create dir static in <project>
- copy css, js, img etc. to <project/static>
- run python manage.py collectstatic

# step by step create apps in django
- create app : python manage.py startapp <nama_app>
- edit file <project>/settings.py INSTALLED APPS tambahkan <nama_app>.apps.<nama_app_config>
- add file urls.py in <nama_app> and edit 
- edit <project>/urls.py
- edit <nama_app>/views.py

	

