# Project_name

Notes and code about project_name

## Sections

- [Project_name](#project_name)
  - [Sections](#sections)
  - [Notes](#notes)
  - [Add PostgreSQL Integration](#add-postgresql-integration)
  - [Django User Management](#django-user-management)
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

.

## Additional Information

### Screenshots

### Links

## Notes template

```python
```

```html

```
