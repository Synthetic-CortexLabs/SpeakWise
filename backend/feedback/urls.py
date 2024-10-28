from django.urls import path
from feedback import views

urlpatterns = [
    path('feedback/', views.list_feedback, name='list_feedback'),
    path('feedback/<str:pk>/', views.feedback_detail, name='feedback_detail'),
]
