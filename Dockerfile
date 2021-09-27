FROM python:3.9.0

WORKDIR /home/

RUN echo 'dkanrjsk1'

RUN git clone https://github.com/TTioTTi/gis_1ban.git

WORKDIR /home/gis_1ban/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 9000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=djangoProject000.settings.deploy && python manage.py migrate --settings=djangoProject000.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=djangoProject000.settings.deploy djangoProject000.wsgi --bind 0.0.0.0:9000"]
