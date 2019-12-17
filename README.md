# Django Docker Deployment

Clone the repo to server and then run the following command


# Development :

Run the migrations 
```sh
docker-compose run app sh -c "python manage.py makemigrations core"
docker-compose run app sh -c "python manage.py migrate"

```
The for running serer
```sh
docker-compose up
```

One its done open your browser and go to 

localhost:8000 you will see the site running

This will be using the docker-compose.yml file and doesnt use nginx , gumtree etc

# Production

Migrations

```sh
docker-compose -f docker-compose.prod.yml run web python manage.py makemigrations core
docker-compose -f docker-compose.prod.yml run web python manage.py migrate

```
Build
```sh
docker-compose -f docker-compose.prod.yml up --build -d
```
For static files 

```sh
docker-compose -f docker-compose.prod.yml run web python manage.py collectstatic --noinput
```
Once its done visit your website
