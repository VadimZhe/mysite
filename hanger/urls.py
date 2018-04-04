from django.urls import path

from . import views

app_name = 'hanger'
urlpatterns = [
	path('', views.initial_view, name='initial_view'),
	path('guess/', views.make_a_guess, name='guess'),
]