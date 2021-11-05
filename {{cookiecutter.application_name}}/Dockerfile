FROM python:3.7.10

LABEL vendor='{{ cookiecutter.full_name }}' \
       mail='{{ cookiecutter.email }}' \
       version='{{ cookiecutter.version }}' \
       release-date='{{ cookiecutter.release_date }}'

RUN apt-get -y update \
       && apt-get install -y locales locales-all \
       && locale-gen en_US.ISO-8859-1 \
       && echo "America/Bogota" > /etc/timezone \
       && dpkg-reconfigure -f noninteractive tzdata \
       && mkdir -p /opt/config  \
       && mkdir -p /opt/files

ENV PYTHONDONTWRITEBYTECODE=1 \
   PYTHONUNBUFFERED=1 \
   DEBIAN_FRONTEND=noninteractive

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./docs/requirements.txt /opt/config/
RUN pip3 install --no-cache-dir --compile -r /opt/config/requirements.txt 

WORKDIR /code

ENTRYPOINT ["python3"]