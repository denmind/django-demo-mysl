# django-demo-mysql
Django tutorial for creating, retrieving, updating and deleting basic records

<admin>
<raspberryberet>

<registrar>
<nsx4H7LFNx8QfvC>

## 1. Install Django
###### Make sure pip is using latest version
    pip install Django

## 2. Install MySQL driver
    pip install mysqlclient

## 3. Create new project
##### Format: 
    django-admin startproject 'projectname'
##### Example: 
    django-admin startproject demo_mysql

## 4. Create a MySQL database
##### Format: 
    CREATE DATABASE 'databasename'
##### Example: 
    CREATE DATABASE demo_django

## 5. Configure project to use MySQL instead of default SQLite
###### Driver
https://pypi.org/project/mysqlclient/
###### Documentation link
https://docs.djangoproject.com/en/3.0/ref/settings/#databases

###### Modify the following lines from projectname/settings.py

##### Format: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': databasename,
            'USER': databaseuser,
            'PASSWORD': databaseuserpassword,
            'HOST': databaseserver,
        }
    }

##### Example:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'demo_django',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
        }
    }


## 6. Create app in your project
##### Format: 
    python manage.py startapp 'appname'
##### Example: 
    python manage.py startapp demo

## 7. Create your models
###### Modify models.py and add your classes
###### Register your model to *admin.py*
##### Format: 
    admin.site.register('modelname')
##### Example: 
    admin.site.register(Person)
###### You can add additional configuration by other another
###### configuration by adding a ModelAdmin
https://docs.djangoproject.com/en/3.0/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin

## 8. Configure your models
###### Modify apps.py and add a class config
###### Add it to the list of INSTALLED_APPS in your settings.py
#### Format: 
    appname.apps.configclass
#### Example:
    demo.apps.PersonConfig

###### Add your appname to INSTALLED_APPS in 'settings.py'

## 9. Make model migrations
    python manage.py makemigrations 'appname'
##### Example:
    python manage.py makemigrations demo
###### Running the command without an appname will make migrations for all apps in INSTALLED_APPS

## 10. Perform SQL Migrate
    python manage.py sqlmigrate 'appname' 'migrationname'
    python manage.py migrate
#### Example:
    python manage.py sqlmigrate demo 0001
    python manage.py migrate

## 11. Create superuser
    python manage.py createsuperuser

###### After running this command you will be prompted to enter username and matching passwords
###### Email is optional

## 12. Customize admin page
https://docs.djangoproject.com/en/3.0/intro/tutorial07/#customize-the-admin-look-and-feel

##### Format: 
    [os.path.join(BASE_DIR, templatesdirpath)]
##### Example:
    [os.path.join(BASE_DIR, 'demo/templates/admin')]

###### Modify TEMPLATES config for settings.py by changing content of DIRS
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'demo/templates/admin')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
###### Make sure APP_DIRS is set to 'True' or overriding HTML views will not take effect

## 12. Login admin
**http://127.0.0.1:8000/admin/**
