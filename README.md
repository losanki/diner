---
layout: post
title:  "notes"
date:   2020-06-24 19:48:56 +0530
categories: jekyll installation
---

Django Diner
======

App for Dining Management 

Install
-------

Create a virtualenv and activate it
```
    $ python3 -m venv venv
    $ . venv/bin/activate
```

Or on Windows
```
    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat
```

Install Django and related dependencies
```
    $ pip install -r requirements.txt
```

Create superuser
```
    $ python manage.py createsuperuser
```

Run
```
    $ python manage.py runserver
``` 

Open http://127.0.0.1:8000 in a browser.

Test
```
    $ python manage.py test
```
