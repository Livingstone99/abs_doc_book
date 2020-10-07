from . import views
from django.urls import path

from .views import  RegisterView,LoginView,AppointmentView

urlpatterns = [
    # path('', views.home, name = 'home'),

    path('register', RegisterView.as_view()),

    path('login', LoginView.as_view()),
    path('booking',AppointmentView.as_view() ),


]