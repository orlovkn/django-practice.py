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
1. [start project](https://realpython.com/customize-django-admin-python/)
1. [forms and fields](https://docs.djangoproject.com/en/3.1/ref/forms/fields/)
1. [urls](https://docs.djangoproject.com/en/3.1/topics/http/urls/)
1. [auth and registration](https://docs.djangoproject.com/en/3.1/topics/auth/default/)
1. [static files](https://docs.djangoproject.com/en/3.1/howto/static-files/)
1. [Common Regular Expressions for Django URLs](https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls)
1. [generic list and detail views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
1. [Large File Uploads with Amazon S3 + Django](https://www.codingforentrepreneurs.com/blog/large-file-uploads-with-amazon-s3-django/)
1. [A Unique Slug Generator for Django](https://www.codingforentrepreneurs.com/blog/a-unique-slug-generator-for-django/)
1. [Random String Generator in Python](https://www.codingforentrepreneurs.com/blog/random-string-generator-in-python/)

1. [Django Admin Cookbook](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/index.html)

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

### filters
```
qs = Product.object.all()
qs = Product.object.get(id=3)
qs = Product.object.filter(id=4)
qs = Product.object.filter(title__contains='hat')
qs = Product.object.filter(description__contains='hat')
qs = Product.object.filter(description__icontains='this')
```