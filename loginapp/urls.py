from django.urls import path
from loginapp import views

urlpatterns = [
    path("",views.LoginView.as_view(), name="login"),
    path("register",views.RegistrationView.as_view(), name="registration"),
    path("signout", views.SignOutView.as_view(), name="signout"),

]