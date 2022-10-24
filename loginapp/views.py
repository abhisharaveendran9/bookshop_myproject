from django.shortcuts import render,redirect
from loginapp import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView,View
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request,"Your account has been created")
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = forms.LoginForm

    def post(self, request, *args, **kw):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
                    # messages.success(request, "successfully login, Welcome ! ")

                    return redirect("home")

            else:
                messages.error(request, "invalid username or password")
                return render(request, "login.html", {"form": form})

        return render(request, "login.html")


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")