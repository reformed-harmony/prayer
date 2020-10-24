FROM alpine:latest
LABEL maintainer="Nathan Osman <nathan@quickmediasolutions.com>"

# Install Python 3 and uWSGI
RUN \
    apk add --no-cache \
        uwsgi-http \
        uwsgi-python \
        py3-pip

# Copy the list of Python packages required for the project
COPY requirements.txt /src/

# Set the working directory to /src
WORKDIR /src

# Install packages necessary for building dependencies and install them
RUN \
    apk add --no-cache \
        build-base \
        libpq \
        postgresql-dev \
        python3-dev && \
    pip install -r requirements.txt && \
    apk del \
        build-base \
        postgresql-dev \
        python3-dev

# Copy the project files
COPY . /src/

# Collect the static files (stored in /srv/static)
RUN SECRET_KEY=x python3 manage.py collectstatic

# Run uWSGI for the application
CMD [ \
    "uwsgi", \
    "--plugin", "python,http", \
    "--http", "0.0.0.0:80", \
    "--module", "prayer.wsgi", \
    "--static-map", "/static=/srv/static", \
    "--static-map", "/media=/data/media" \
    ]
