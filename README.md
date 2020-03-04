# Stayln

Course project for Columbia University COMS W6998 - Cloud Computing and Big Data, 2020 Spring.

## Team Members
- [Cunjun Wang](https://github.com/CunjunWang) (UNI: cw3199)
- [Jiefan Li](https://github.com/Jason003) (UNI: jl5501)
- [Jierui Liu](https://github.com/Willincia1124) (UNI: jl5490)
- [Jingkaihui Wei](https://github.com/jingkaw) (UNI: jw3826)

## Set Up and Run
```
git clone git@github.com:CunjunWang/stayln-service.git
cd stayln-service
git switch dev (remove it in production)
cd stayln 
```
Please create a postgreSQL database called staylndb and modify the stayln/settings.py to change the following part according to your postgreSQL settings 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'staylndb',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost'
    }
}
```
Then, run
```
python manage.py migrate
python manage.py runserver
```
Then, you can access development server at http://127.0.0.1:8000/
## Project Description

## Document

## Comment
