
from django.contrib import admin
from django.urls import path ,include
from FoodApp import views
urlpatterns = [
    path('add_food_details/', views.add_food_details),
    path('add_food_details_post/', views.add_food_details_post),
    path('view_food_details/', views.view_food_details),
    path('edit_post/', views.edit_post),
    path('delete_view_food_details/<id>', views.delete_view_food_details),
    path('edit/<id>', views.edit),
    path('home_page/', views.home_page),
    path('add_category/', views.add_category),
    path('category_post/', views.category_post),
    path('view_category/', views.view_category),
    path('edit_category_post/', views.edit_category_post),
    path('delete_category/<id>', views.delete_category),
    path('edit_category/<id>', views.edit_category),
    path('admin_home/', views.admin_home),
    path('login_post/', views.login_post),
    path('login_page/', views.login_page),

    path('register_user/', views.register_user),
    path('register_user_post/', views.register_user_post),
    path('view_user_details/', views.view_user_details),
    path('user_make_order/<id>', views.user_make_order),
    path('user_make_order_post/', views.user_make_order_post),
    path('view_order_details/', views.view_order_details),

    path('admin_view_orders/', views.admin_view_orders),
]
