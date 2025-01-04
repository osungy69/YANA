FROM python:3.10

WORKDIR /home/

RUN echo "testing3"

RUN git clone https://github.com/osungy69/project1.git

WORKDIR /home/project1/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=project1.settings.deploy && python manage.py migrate --settings=project1.settings.deploy && gunicorn project1.wsgi --env DJANGO_SETTINGS_MODULE=project1.settings.deploy --bind 0.0.0.0:8000"]