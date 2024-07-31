from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.AllProfiles.as_view()),
    path('users/<int:pk>/', views.OneProfile.as_view()),
]
