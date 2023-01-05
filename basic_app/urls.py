from django.urls import path

from basic_app import views

urlpatterns = [
    path('user/', views.ListMy.as_view()),
    path('user/<int:pk>', views.DetailMy.as_view())
]
