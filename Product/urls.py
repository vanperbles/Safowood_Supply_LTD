from django.urls import path
from Product import views
app_name = 'item'
urlpatterns =[
    path('',views.ItemListView.as_view(), name='index'),
    path('item/<slug>',views.ItemDetailView.as_view(),name='detail'),
    path('item/create/new', views.ItemCreateView.as_view(), name='new_item'),
    path('item/<slug>/update', views.ItemUpdateView.as_view(), name='update_item'),
    path('item/<slug>/delete', views.ItemDeleteView.as_view(), name='delete_item'),
    path('search/', views.Search, name='search'),

]