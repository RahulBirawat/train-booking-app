from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('book/',views.book,name="book"),
    # path('search/',views.search_trains,name="search_trains"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('display/',views.search_trains,name="search_trains"),
]