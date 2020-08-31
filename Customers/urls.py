from django.urls import path
from Customers import views

app_name = 'customer'


urlpatterns = [
    path('new/',views.myCustomer,name='new_customer')


]