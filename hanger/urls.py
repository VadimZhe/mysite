from django.urls import path

from . import views

app_name = 'hanger'
urlpatterns = [
	path('', views.simple_view, name='simple_view'),
	path('guess_made/', views.make_a_guess, name='guess_made'),
]