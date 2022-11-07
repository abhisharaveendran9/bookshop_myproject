from django.shortcuts import render,redirect
from loginapp import forms
from customer import forms
from django.contrib import messages
from django.urls import reverse_lazy
from owner.models import Books,Carts,Orders
from django.views.generic import TemplateView,View,DetailView,FormView,ListView
from django.contrib.auth import logout
# Create your views here.


class HomeView(TemplateView):
    template_name: str="home.html"




class BooksListView(View):

    def get(self, request, *args, **kwargs):
        all_books = Books.objects.all()
        return render(request, "all-books.html", {"books": all_books})


class BookDetailView(DetailView):
    template_name: str="book-details.html"
    model=Books
    context_object_name="book"
    pk_url_kwarg: str="id"



class AddToCartView(FormView):
    template_name: str="addto-cart.html"
    form_class=forms.CartForm

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)

        return render(request,self.template_name,{"form":forms.CartForm(),"book":book})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(book=book,user=user,qty=qty)
        # messages.success(request,"successfully your product hasbeen added to cart")
        return redirect("home")

class MyCartView(ListView):    #cart listview
    model=Carts
    template_name: str="cart-list.html"
    context_object_name="carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).order_by("-created_date")


class PlaceOrderView(FormView):
    template_name: str = "place-order.html"
    form_class = forms.OrderForm

    def post(self, request, *args, **kwargs):
        cart_id = kwargs.get("cid")
        product_id = kwargs.get("pid")
        cart = Carts.objects.get(id=cart_id)
        book = Books.objects.get(id=product_id)
        user = request.user
        delivery_address = request.POST.get("delivery_address")
        Orders.objects.create(book=book,
                              user=user,
                              delivery_address=delivery_address

                              )
        cart.status = "order-placed"
        cart.save()
        # messages.success(request, "successfully your order hasbeen placed")
        return redirect("home")

def delete_product(request,*args,**kwargs):  #product status:cancelled only
    id=kwargs.get("id")
    cart=Carts.objects.get(id=id)
    cart.status="cancelled"
    cart.save()
    return redirect("mycart")


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
