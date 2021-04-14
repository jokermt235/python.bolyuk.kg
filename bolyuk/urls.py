from django.urls import path
from . import views
urlpatterns = [
    path('categories/create', views.CategoryCreateView.as_view()),
    path('categories/all', views.CategoryListView.as_view()),
    path('categories/detail/<int:pk>/', views.CategoryDetailView.as_view()),
]