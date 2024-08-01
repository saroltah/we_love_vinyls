from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.AllLikes.as_view()),
    path('likes/<int:pk>/', views.OneLike.as_view()),
    path('attendance/', views.AllAttendance .as_view()),
    path('attendance/<int:pk>/', views.OneAttendance.as_view()),
]
