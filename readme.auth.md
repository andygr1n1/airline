python manage.py startapp users
settings -> users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include('flights.urls')),
    path('users/', include('users.urls')),
]

create a new urls.py
