## RH Prayer Website

TODO

### Deploying in Production

The prayer app is designed to run in Docker with the [postgres](https://hub.docker.com/_/postgres) and [hectane](https://hub.docker.com/r/hectane/hectane) containers. Configuration is provided through the following environment variables:

Name | Description | Default
--- | --- | ---
DB_NAME | *set to the name of the PostgreSQL database* | postgres
DB_USER | *set to the username for connecting to PostgreSQL* | postgres
DB_PASSWORD | *set to the password for connecting to PostgreSQL* | *blank*
DB_HOST | *set to the hostname of the PostgreSQL server* | postgres
DEBUG | *set to any value to enable debug mode for local development* | *none*
HECTANE_HOST | *set to the hostname of the Hectane server* | hectane
SECRET_KEY | *set to a reasonably long string of random ASCII characters* | *blank*
SITE_NAME | *set to the human-readable name of the website* | "RH Prayer"
SITE_DOMAIN | *set to the domain name of the website* | prayer.quickmediasolutions.com
