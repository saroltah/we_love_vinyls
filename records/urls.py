from django.urls import path
from records import views

urlpatterns = [
    path('records/', views.AllRecords.as_view()),
    path('records/<int:pk>/', views.OneRecord.as_view()),
]
