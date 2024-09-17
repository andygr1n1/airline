from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),  # This renders the index page
    path('flight/<int:id>/', views.flight_view, name='flight'),  # Individual flight detail page
    path('flight/<int:id>/book/', views.book_view, name='book'),  # Booking page for a flight
]