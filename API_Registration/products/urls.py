from django.urls import path
from . import views

urlpatterns = [

    path('<int:id>', views.details, name='details'),
    path('all', views.show_products, name='show_products'),
    path('add' , views.add , name='add')

]
