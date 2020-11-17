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
  - [Work With Django User Management](#work-with-django-user-management)
    - [Create a login page](#create-a-login-page)
    - [Create a Logout Page](#create-a-logout-page)
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
- Create a base template
- Create a `dashboard.html` file
- Display the current user's username and set a default with `{{ user.username | default:"Guest" }}`

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<body>
  <main>
    <vstack spacing="m">
      <vstack spacing="s" stretch="" align-x="center" align-y="center">
        <h1>Django-Users</h1>
        <h2>Hello {{ user.username | default:"Guest" }}!</h2>
      </vstack>
      <spacer></spacer>
      <vstack spacing="l">
        <vstack spacing="xs">
          <aside class="pa-s">
            <vstack>
            </vstack>
          </aside>
        </vstack>
      </vstack>
    </vstack>
  </main>
</body>
{% endblock header_content %}
```

- If the user isn’t logged in, then Django will still set the user variable using an `AnonymousUser` object. An anonymous user always has an empty username, so the dashboard will show `Hello, Guest!`
- Create a view to render it

```python
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, "dashboard.html", {})
```

- Set an url to access the view

```python
from django.urls import path

from django_users import views

app_name = "django_users"

urlpatterns = [path("dashboard/", views.dashboard, name="dashboard")]
```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_users.urls", namespace="django_users")),
]
```

## Work With Django User Management

- Django has a lot of user management–related resources that’ll take care of almost everything, including login, logout, password change, and password reset. Templates aren’t part of those resources, though. You have to create them on your own.

- Add the URLs provided by the Django authentication system into the app urls

```python
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
]
```

### Create a login page

- For the login page, Django will try to use a template called `registration/login.html`

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<body>
  <main>
    <vstack spacing="m">
      <vstack spacing="s" stretch="" align-x="center" align-y="center">
        <h1>Django-Users: Login</h1>
        <h2>Hello {{user.username|default:"Guest"}}!</h2>
      </vstack>
      <spacer></spacer>
      <vstack spacing="l">
        <vstack spacing="xs">
          <aside class="pa-s">
            <vstack>
              <form method="POST">
                {% csrf_token %} {{form.as_p}}
                <input type="submit" value="login" />
              </form>
              <a href="{% url 'django_users:dashboard' %}">Back to dashboard</a>
            </vstack>
          </aside>
        </vstack>
      </vstack>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

- Django will automatically create the view and urls necessary for the template.
- Redirect to dashboard in settings

```python
LOGIN_REDIRECT_URL = "django_users:dashboard"
```

### Create a Logout Page

- Users can log in, but they should also be able to log out. This process is more straightforward because there’s no form—they just need to click a link. After that, Django will redirect users to `accounts/logout` and will try to use a template called `registration/logged_out.html`.
- Redirect them to the dashboard

```python
LOGOUT_REDIRECT_URL = "django_users:dashboard"
```

- Add logout and login links to dashboard

```html
<hstack spacing="s">
        <h2>Hello {{user.username|default:"Guest"}}!</h2>
        <span>
            {% if user.is_authenticated %}
            <a href="{% url 'django_users:logout' %}">Logout</a>
            {% else %}
            <a href="{% url 'django_users:login' %}">Login</a>
            {% endif %}
        </span>
        </hstack>
```



## Additional Information

### Screenshots

### Links

## Notes template

```python
```

```html

```
