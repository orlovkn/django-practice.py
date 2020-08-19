## Build a Django eCommerce Web Application with Python

### install Django [on Linux Ubuntu](https://www.codingforentrepreneurs.com/blog/install-django-on-linux-ubuntu/)
```
python3 -m pip install Django
```

### create new folder for project
```
mkdir ecommerce
cd ecommerce
pwd
```

### create venv
```
virtualenv -p python3 .
```

### activate venv
```
source bin/activate
```

### run server
```
python3 manage.py runserver
python3 manage.py runserver 8888
```

### collect static
```
python3 manage.py collectstatic
```

### links
1. [forms and fields](https://docs.djangoproject.com/en/3.1/ref/forms/fields/)
1. [auth and registration](https://docs.djangoproject.com/en/3.1/topics/auth/default/)
1. [static files](https://docs.djangoproject.com/en/3.1/howto/static-files/)

