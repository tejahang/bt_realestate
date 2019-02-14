from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.single_listing, name='single_listing'),
    path('search', views.search, name='search')
]