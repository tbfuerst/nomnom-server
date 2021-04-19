# nomnom-server
A Django Server to serve NomNom as a Backend, communicating via REST API (DRF)
Additionally there is a Flutter Web Frontend hosted.

Help with Setting up the Dockerfile and docker-compose: https://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/

This is a dockerized Django Server for the NomNom Cookbook App..

To Install, follow these steps:

1. Make Sure, that the following Settings are made in nomnom_server/settings.py
    -   WSGI_APPLICATION = 'nomnom_server.wsgi.application'
    -   STATIC_URL = 'nomnom/static/'
    -   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'nomnom/static')]
    -   ALLOWED_HOSTS = ['...'] -> the DNS you want (see Step 9)

2. Set up Postgres Credentials at nomnom_server/settings.py

3. Create a new user at the linux shell

4. Execute ./build-container

5. Access Database Service with ./open-db and Create A Database and User according to nomnom_server/settings.py
    5.1     psql
    5.2     CREATE DATABASE [dbname];
    5.3     CREATE USER username WITH PASSWORD 'abc';
    5.4     ALTER DATABASE [dbname] OWNER TO [user];  

6. Access Django Server with ./access-api
    6.1 Change to App directory at /opt/app
    6.2 Execute python3 manage.py migrate
    6.3 Create a Superuser with python3 manage.py createsuperuser

7. (Optional) Place the Web Frontend in nomnom/static

8. (Optional) Execute ./collectstatic if you want to Use the Web Frontend

9. Set up an Apache / Nginx Proxy and place it before the WSGI server, which defaults to Port 8100

10. Visit https://your.url.com/admin to Create Users

11. Visit https://your.url.com/o/applications to register your client with OAuth



Database setup

1   apt-get install python3
2   apt-get install pip3
3   pip3 install psycopg2
4   apt-get install postgresql postgresql-contrib
    4.0 Access DB sudo su postgres -> psql
    4.1 See Databases \l
    4.2 See Users  \du
    4.3 Change passwords  ALTER USER user WITH PASSWORD 'my_password';
    4.4 Superuser  ALTER USER my_user WITH SUPERUSER;
    4.5 login as user psql -U my_user
    4.6 if login dont work: change /etc/postgresql/11/main/pg_hba.conf  (auth method peer -> md5) FOR LOCAL, not administrative users, then sudo service postgresql restart
5   Create new postgres user
    5.1     su postgres
    5.2     psql
    5.3     CREATE DATABASE [dbname];
    5.4     CREATE USER username WITH PASSWORD 'abc';
    5.5     ALTER DATABASE [dbname] OWNER TO [user];
6 Useful Database Commands
    6.1 \c [database name] - connect to database
    6.2 \l  list all Databases
    6.3 \du list all users
    6.4 \dt list all tables of connected DB
7 Model change:
    Change your models (in models.py).
    Run python manage.py makemigrations [project] to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.
8 Migrate a certain Migration: python3 manage.py migrate
    8.1 Before Migration: Check for errors with python3 manage.py check nomnom
    8.2 check SQL output with python3 manage.py sqlmigrate nomnom [number of migration] (doesnt migrate!)
9 Directly access API with python3 manage.py shell
    9.1 from nomnom.models import [model1], [model2]
10 run python3 manage.py dbseed to add some mock data

Deploying the app:
https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
https://nosynerds.com/build-and-deploy-a-rest-api-with-django-and-docker-part-4/