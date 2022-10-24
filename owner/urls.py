from django.urls import path
from owner import views


urlpatterns=[
    path("dashboard", views.AdminDashBoardView.as_view(), name="dashboard"),
    path("category",views.CategoryAddView.as_view(), name="category"),
    path("book",views.BookAddView.as_view(), name="book"),
    path("category/list", views.CategoryListView.as_view(), name="categorylist"),
    path("category/change/<int:id>", views.CategoryEditView.as_view(), name="category-edit"),
    path("category/remove/<int:id>",views.delete_category,name="remove-category"),
    path("book/list", views.BookListView.as_view(), name="booklist"),
    path("book/remove/<int:id>",views.delete_book,name="remove-book"),
    path("book/details/<int:id>",views.BookDetailView.as_view(),name="book-detail"),
    path("book/change/<int:id>",views.BookEditView.as_view(),name="book-edit")

]