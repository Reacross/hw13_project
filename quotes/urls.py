from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"), # quotes:root
    path('<int:page>', views.main, name="root_paginate"), # quotes:root_paginate
    path('add_author/', views.add_author, name="add_author"), # quotes:add_author
    path('add_quote/', views.add_quote, name="add_quote"), # quotes:add_quote
    path('author/<int:id>', views.author_info, name="author_info"), #quotes:author_info
]
