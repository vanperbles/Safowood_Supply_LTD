from django.urls import path
from . import views
app_name = 'myAuth'

urlpatterns = [
    # path('', views.Index, name = "index"),
    path('login/', views.login_page, name='login'),
    # path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]