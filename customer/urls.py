from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.HomeView.as_view(), name="home"),

]