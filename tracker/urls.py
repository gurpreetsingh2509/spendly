from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:id>/edit/', views.edit_expense, name='edit_expense'),
    path('expenses/<int:id>/delete/', views.delete_expense, name='delete_expense'),
]
