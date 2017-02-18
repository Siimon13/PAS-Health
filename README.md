# python-getting-started

Barebone WebApp

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org)
```sh
$ git clone https://github.com/Siimon13/PAS-Health.git
$ cd PAS-Health

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Documentation

The app is based in pas
The static folder is in gettingstarted(For imgs/js/css)

The templates have examples of loading static and forms

All code is ran through view.py(controller)

Making a new form requires you to add a valid form to form.py [Read More](https://docs.djangoproject.com/en/1.10/topics/forms/)

If you want to use a database, use model.py [Read More](https://docs.djangoproject.com/en/1.10/topics/db/models/)