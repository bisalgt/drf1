from django.urls import path

from apis.quiz import views


urlpatterns = [
	path('', views.home),
	path('home/', views.HomeView.as_view()),
]