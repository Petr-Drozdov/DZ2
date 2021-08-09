from django.urls import path

from MainApp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('item/', views.items),
    path('items/', views.items),
    path('item/<int:id>', views.item_details),

]
