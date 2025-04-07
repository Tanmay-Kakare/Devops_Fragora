
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.product, name='products'),
    path('add_to_cart/<int:perfume_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.view_cart, name='cart'),
    path('update_cart/<int:order_id>/', views.update_cart, name='update-cart'),
    path('delete_cart/<int:order_id>/', views.delete_from_cart, name='delete-cart'),
    path('cart/empty/', views.empty_cart, name='empty-cart'),

#account 
   path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('account/update/', views.update_account, name='update-account'),
    path('delete-account/', views.delete_account, name='delete-account'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
