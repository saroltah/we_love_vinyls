from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.AllComments.as_view()),
    path('comments/<int:pk>/', views.OneComment.as_view())
]
