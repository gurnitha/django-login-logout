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