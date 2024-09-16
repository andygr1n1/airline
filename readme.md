django-admin startproject myproject

python manage.py startapp flights

python manage.py runserver

python manage.py migrate

python manage.py createsuperuser



1. settings setup app
2. urls setup urls
3. create urls.py in flights app

python manage.py makemigrations
python manage.py migrate
python manage.py shell

from flights.models import Flight
f = Flight(origin="New York", destination="London", duration=415)
f = Flight(origin="Shanghai", destination="Paris", duration=760)
f = Flight(origin="Istanbul", destination="Tokyo", duration=700)
<!-- Flight.objects.all().delete() -->
f.save()

Flight.objects.all()



<!-- 
flights = Flight.objects.all()

print(flights) -->

from flights.models import *

Airport.objects.filter(city="New York").first()
airport = Airport.objects.get(city="New York")

jfk = Airport.objects.get(city="New York")
cdg = Airport.objects.get(city="Paris")
f = Flight(origin=jfk, destination=cdg, duration=435)
f.save()
flights = Flight.objects.all()

for flight in flights:
    print(f"{flight.origin} to {flight.destination}")

<!--  -->
<!--  -->
<!--  -->
python manage.py createsuperuser
andreigrini
grini