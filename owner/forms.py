from django import forms
from owner.models import Categories,Books
from django.forms import ModelForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=[
            "category_name",
            "is_active"
        ]
        widgets={
            "category_name" : forms.TextInput(attrs={"class": "form-control"}),
            "is_active":forms.CheckboxInput()
        }


class CategoryChangeForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=[
            "category_name","is_active"
        ]
        widgets={
            "category_name" : forms.TextInput(attrs={"class": "form-control"}),
            "is_active":forms.CheckboxInput()
        }


class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=[
            "book_name","author","category","image","price","description"
        ]

        widgets={
            "book_name":forms.TextInput(attrs={"class": "form-control"}),
            "author":forms.TextInput(attrs={"class": "form-control"}),
            "category":forms.Select(attrs={"class": "form-control"}),
            "image":forms.ClearableFileInput(attrs={"class": "form-control"}),
            "price":forms.TextInput(attrs={"class": "form-control"}),
            "description":forms.Textarea(attrs={"class": "form-control"}),

        }


class BookChangeForm(forms.ModelForm):
    class Meta:
        model=Books
        fields = [
            "book_name", "author", "category", "image", "price", "description"
        ]

        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),

        }


class OrderUpdateForm(forms.Form):
    options={
        ("dispatched","dispatched"),
        ("in-transit","in-transit")
    }
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"}))
    expected_delivery_date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
