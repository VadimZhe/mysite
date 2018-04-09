from django.urls import path

from . import views

app_name = 'hanger'
urlpatterns = [
	#path('', views.initial_view, name='initial_view'),
	path('', views.make_a_guess_sync, name='initial'),
	path('async/', views.make_a_guess_async, name='async'),
	path('asyncret/', views.get_secret, name='secret'),
	#path('guess/', views.make_a_guess_sync, name='guess'),
	#path('showme/', views.show_me_func, name = 'showme')
]