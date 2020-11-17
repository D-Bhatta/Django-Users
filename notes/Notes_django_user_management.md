# Project_name

Notes and code about project_name

## Table of Contents

.

## Sections

.

## Notes

Note information.

## Add PostgreSQL Integration

1. .
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

## Additional Information

### Screenshots

### Links

## Notes template

```language

```
