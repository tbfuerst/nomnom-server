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

