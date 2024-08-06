from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('overview/', views.overview, name='overview'),

    path('prices', views.prices, name='prices'),

    path('search/<str:query>/', views.search, name='search'),
]
