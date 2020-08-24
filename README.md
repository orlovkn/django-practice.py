## Build a Django eCommerce Web Application with Python

### install Django [on Linux Ubuntu](https://www.codingforentrepreneurs.com/blog/install-django-on-linux-ubuntu/)
```
python3 -m pip install Django
```

### create new folder for project
```
mkdir ecommerce
cd ecommerce
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
1. [Common Regular Expressions for Django URLs](https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls)
1. [Generic list and detail views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)

### create an app
```
python3 manage.py startapp + name
```

### CRUD
```
Create — POST
Retrieve / List / Search — GET
Update — PUT / Patch / POST
Delete — DELETE
```

### rules
after all new model changes you should do this
```
python3 manage.py makemigrations
python3 manage.py migrate
```