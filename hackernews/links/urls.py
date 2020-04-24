from django.urls import path, include
from . import views 


urlpatterns=[
    path('', views.home, name='home'),
    path('submission/', views.link_submit, name='link_submit'),
    path('link/<int:id>/', views.link_view, name='link_view'),
]