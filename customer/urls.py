from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.HomeView.as_view(), name="home"),
    path("books/list", views.BooksListView.as_view(), name="all-books"),
    path("books/<int:id>", views.BookDetailView.as_view(), name="book-details"),
    path("books/<int:id>/carts/add", views.AddToCartView.as_view(), name="addto-cart"),
    path("carts/all", views.MyCartView.as_view(), name="mycart"),
    path("carts/placeorder/<int:cid>/<int:pid>", views.PlaceOrderView.as_view(), name="place-order"),
    path("carts/remove/<int:id>", views.delete_product, name="remove-item"),
    path("signout", views.SignOutView.as_view(), name="signout"),

]