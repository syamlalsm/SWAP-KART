from django.urls import path
from . import views

urlpatterns = [
    path('brands/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('navbar',views.navbar,name='navbar'),
    path('footer',views.footer,name='footer'),
    path('',views.brand_list, name='brand_list'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('add_brand_model/', views.add_brand_model, name='add_brand_model'),
    path('brand_model/<str:name>/', views.brand_model_detail, name='brand_model'),
    path('checkout',views.checkout,name='checkout'),
    path('success/', views.success, name='success'),
]