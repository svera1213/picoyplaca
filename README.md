# Pico y placa predictor
 
## Add .env file

POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=

## Run the following (for the first time)

- sudo docker-compose up
- sudo docker-compose run web python manage.py migrate
- sudo docker-compose run web python manage.py migrate picoplacapredictor
- sudo docker-compose run web python manage.py generate_test_data

## Call Endpoint

GET http://0.0.0.0:8000/api/predictor/plates/<str: plate>?search_date=YYYY-MM-DD&search_time=HH:MM:SS
