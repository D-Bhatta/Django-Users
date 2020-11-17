# Project_name

Notes and code about project_name

## Sections

- [Project_name](#project_name)
  - [Sections](#sections)
  - [Notes](#notes)
  - [Add PostgreSQL Integration](#add-postgresql-integration)
  - [Django User Management](#django-user-management)
    - [Create an app `django_users`](#create-an-app-django_users)
    - [Disable password validators in settings. Just comment them out, leaving an empty list](#disable-password-validators-in-settings-just-comment-them-out-leaving-an-empty-list)
    - [Create a superuser](#create-a-superuser)
  - [Create a Dashboard View](#create-a-dashboard-view)
  - [Additional Information](#additional-information)
    - [Screenshots](#screenshots)
    - [Links](#links)
  - [Notes template](#notes-template)

## Notes

Notes about Django User Management.

## Add PostgreSQL Integration

1. Change settings to use PostgreSQL instead of SQLite
2. Install `travis` gem using    ```❯ gem install travis```

3. Log into travis with ```❯ travis login --pro --github-token  token```
4. Add the DB information using

    ```bash
    travis encrypt --pro DBNAME="name"  --add

    travis encrypt --pro DBUSER="user"  --add

    travis encrypt --pro DBPASSWORD="password"  --add

    travis encrypt --pro DBHOST="host"  --add

    travis encrypt --pro DBPORT="port"  --add

    ```

5. Push to TravisCI

## Django User Management

### Create an app `django_users`

```bash
> python.exe manage.py startapp django_users
```

### Disable password validators in settings. Just comment them out, leaving an empty list

```python
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]
```

### Create a superuser

```bash
python manage.py createsuperuser
```

## Create a Dashboard View

- Most user management systems have some sort of main page, usually known as a dashboard.
-

## Additional Information

### Screenshots

### Links

## Notes template

```python
```

```html

```
