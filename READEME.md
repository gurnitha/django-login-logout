## CLONE AMAZON USING DJANGO


## 0. SOURCES

#### 0.1.1 Links to source on Github and Youtube

	https://github.com/gurnitha/django-amazon-clone
	https://www.youtube.com/channel/UCyz5M_3Rv2jLUDs4R_yRBkw

## 1. INITIAL SETUP

#### 1.1.1 Create virtual environment and install django

## 2. CREATE DJANGO PROJECT AND DJANGO APP

#### 2.1.2 Create django project 'src-renewed/config'

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders> mkdir src-renewed
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders> cd .\src-renewed\
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> django-admin startproject config . 

#### 2.2.3 Create database and run server

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py makamigrations
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py migrate
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py runserver 

#### 2.3.4 Create django app 'app/main'

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> mkdir app\main
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py startapp main app/main

#### 2.4.5 Install main app to the config project and check for error 

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py check
	System check identified no issues (0 silenced).


## 3. HOME LOGIN PAGES

#### 3.1.6 Create views, templates, urls and render Home page

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> mkdir templates/main
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> touch templates/main/home.html
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> touch templates/base.html
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py check
	System check identified no issues (0 silenced).

#### 3.2.7 Create Login page and add navbar to link Home and Login pages

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> touch .\templates\main\login.html

#### 3.3.8 Modified README.md 


## 4. ADMIN / BACKEND

#### 4.1.9 Create app 'app/backend'

(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> mkdir app/backend
(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py startapp backend app/backend

#### 4.2.10 Install 'backend' to the project 'config' and run check

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py check
	System check identified no issues (0 silenced).

## 5. LOGIN AND LOGOUT PROCESS

#### 5.1.11 Create CustomeUser model, register CustomUser to project's settings.py, and run migrations and createsuperuser

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py makemigrations
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py migrate
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py createsuperuser
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> python manage.py check
	System check identified no issues (0 silenced).

#### 5.2.12 Modified README.md	

#### 5.3.13 Create admin Home page

	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> mkdir .\templates\backend
	(venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src-renewed> touch .\templates\backend\home.html


#### 5.4.14 REDIFINED login

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   config/urls.py
        new file:   templates/backend/login.html
        new file:   templates/backend/login_process.html
        modified:   templates/base.html
        deleted:    templates/main/login.html

#### 5.5.15 Admin home - link and rendering admin Home page

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   config/urls.py
        modified:   templates/base.html

#### 5.6.16 Login - Login process with {% csrf_token %} added

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   config/urls.py
        modified:   templates/backend/login.html

#### 5.7.17 Login - Authenticate user login

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   db.sqlite3

#### 5.8.17 Login - Displaying logged in username on navabar

        modified:   READEME.md
        modified:   templates/base.html

#### 5.9.18 Logout - Create logout method and url path

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   config/urls.py
        modified:   db.sqlite3
        modified:   templates/base.html

#### 5.10.19 Limiting the access to admin dashboard, only logged in user could access it

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   db.sqlite3

#### 5.11.20 Messages - User Login error and Logout success

        modified:   app/backend/__pycache__/views.cpython-39.pyc
        modified:   db.sqlite3
        modified:   templates/backend/login.html


#### 5.12.21 Messages - Login success

        modified:   READEME.md
        modified:   app/backend/views.py
        modified:   db.sqlite3
        modified:   templates/backend/home.html

#### 5.13.22 Styling the project 

        modified:   READEME.md
        modified:   db.sqlite3
        modified:   templates/backend/login.html
        modified:   templates/base.html




























































