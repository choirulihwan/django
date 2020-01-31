# django
list of django based app:
1. Real estate App (python 3.7, mysql, django3.0)

# django documentation
https://docs.djangoproject.com

# step by step django
- installl python
- install pycharm
- setting venv and interpreter
- install django
- create project django : 
- start server 	: python manage.py runserver

# install mysql in django 
- pip install mysqlclient
- if there is error message: OSError: mysql_config not found do sudo apt-get install libmariadbclient-dev
- if there is error message: MySQLdb/_mysql.c:38:10: fatal error: Python.h: No such file or directory do sudo apt install python-dev (https://blog.ducthinh.net/gcc-no-such-file-python-h/)
- configure database in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
- for more details visit: https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04

# error
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'

# solution
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}


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

	

