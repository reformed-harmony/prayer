## RH Prayer Website

TODO

### Local Development

The application is written in Python 3 and uses the [Django](https://www.djangoproject.com/) web framework. You will need to complete the following steps in order to run the project locally:

1. Ensure that [Python](https://www.python.org/) is installed and use [virtualenv](https://virtualenv.pypa.io/en/latest/) to create a new Python environment

1. Install the required dependencies with:

       pip install -r requirements.txt

1. Enable debug mode with:

       set DEBUG=1

1. Initialize the default SQLite database with:

       python manage.py migrate

1. Launch the development server with:

       python manage.py runserver

### Deploying in Production

The prayer app is designed to run in Docker with the [postgres](https://hub.docker.com/_/postgres) and [hectane](https://hub.docker.com/r/hectane/hectane) containers. Configuration is provided through the following environment variables:

Name | Description | Default
--- | --- | ---
DATA_DIR | *set to the directory used for storage* | /data
DB_NAME | *set to the name of the PostgreSQL database* | postgres
DB_USER | *set to the username for connecting to PostgreSQL* | postgres
DB_PASSWORD | *set to the password for connecting to PostgreSQL* | *blank*
DB_HOST | *set to the hostname of the PostgreSQL server* | postgres
DEBUG | *set to any value to enable debug mode for local development* | *none*
HECTANE_HOST | *set to the hostname of the Hectane server* | hectane
SECRET_KEY | *set to a reasonably long string of random ASCII characters* | *blank*
SITE_NAME | *set to the human-readable name of the website* | RH Prayer
SITE_DOMAIN | *set to the domain name of the website* | prayer.quickmediasolutions.com

Note that **SECRET_KEY** is the only variable that *must* be set.
