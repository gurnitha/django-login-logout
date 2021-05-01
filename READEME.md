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