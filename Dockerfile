FROM python:3.10

WORKDIR /home/

RUN git clone https://github.com/osungy69/project1.git

WORKDIR /home/project1/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure--dm1j8=i7#rx&h5b#8yk3)%$e3-p!2$*ju9ot$wg)m-di*6)1m" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]