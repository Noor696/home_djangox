from django.urls import path  # 1. import any thing built in django
from .views import HomeListView, HomeDetailView , HomeCreateView, HomeUpdateView, HomeDeleteView 

urlpatterns = [
    path('home/', HomeListView.as_view(),name="home_list"),
    path('home/<int:pk>', HomeDetailView.as_view(),name="home_detail"),
    path('home/create/', HomeCreateView.as_view(),name="home_create"),
    path('home/<int:pk>/update/', HomeUpdateView.as_view(),name="home_update"),
    path('home/<int:pk>/delete/', HomeDeleteView.as_view(),name="home_delete"),
]