from django.urls import path
from markets import views

urlpatterns = [
    path('markets/', views.AllMarkets.as_view()),
    path('markets/<int:pk>/', views.OneMarket.as_view()),
]
