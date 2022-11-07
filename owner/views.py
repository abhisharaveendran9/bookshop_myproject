from django.shortcuts import render,redirect
from owner import forms
from django.views.generic import CreateView,TemplateView,FormView,View,DetailView,UpdateView,ListView
from owner.models import Categories,Books,Orders
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from owner.forms import CategoryForm, BookForm

# Create your views here.

class AdminDashBoardView(TemplateView):
    template_name: str="dashboard.html"


class CategoryAddView(CreateView):
    model = Categories
    form_class = forms.CategoryForm
    template_name : str= "add-category.html"
    success_url = reverse_lazy("categorylist")

    def form_valid(self, form):
        messages.success(self.request,"new category has been added")
        return super().form_valid(form)

class BookAddView(FormView):
    model = Books
    form_class = forms.BookForm
    template_name: str="add-book.html"

    def post(self,request,*args,**kw):
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            book_name = form.cleaned_data.get("book_name")
            author = form.cleaned_data.get("author")
            category = form.cleaned_data.get("category")
            image = form.cleaned_data.get("image")
            price = form.cleaned_data.get("price")
            description = form.cleaned_data.get("description")
            obj = Books.objects.create(
                book_name=book_name,
                author=author,
                category=category,
                image=image,
                price=price,
                description=description,
            )
            obj.save()
            return render(request, "dashboard.html")


class CategoryListView(View):

    def get(self,request,*args,**kwargs):
        all_category=Categories.objects.all()
        return render(request,"categorylist.html",{"categories":all_category})

class CategoryEditView(UpdateView):
    model = Categories
    form_class = forms.CategoryForm
    template_name = "category-edit.html"
    success_url = reverse_lazy("categorylist")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        return super().form_valid(form)


def delete_category(request, *args, **kwargs):
    id=kwargs.get("id")
    Categories.objects.get(id=id).delete()
    # messages.success(request,"deleted")
    return redirect("categorylist")



class BookListView(View):

    def get(self,request,*args,**kwargs):
        all_books=Books.objects.all()
        return render(request,"booklist.html",{"books":all_books})



class BookDetailView(DetailView):
    model=Books
    context_object_name = "book"
    template_name = "book-detail.html"
    pk_url_kwarg = "id"



class BookEditView(UpdateView):
    model = Books
    form_class = forms.BookForm
    template_name = "book-edit.html"
    success_url = reverse_lazy("booklist")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        return super().form_valid(form)


def delete_book(request, *args, **kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    # messages.success(request,"deleted")
    return redirect("booklist")


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")


class OrdersListView(ListView):
    model=Orders
    context_object_name="orders"
    template_name: str="admin-orderlist.html"

    def get_queryset(self):
        return Orders.objects.filter(status="order-placed")