from django.urls import path
from . import views as ev

urlpatterns=[
    path('',ev.home,name='home'),
    path('register',ev.register,name='register'),
    path('login/',ev.login_page,name='login'),
    path('logout/',ev.logout_page,name='logout'),
    path('collections/',ev.collections,name='collections'),
    path('collections/<str:name>',ev.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',ev.product_details,name='product_details'),
    path('addtocart',ev.add_to_cart,name='addtocart'),
    path('cart/',ev.cart_page,name='cart'),
    path('removecart/<str:cid>',ev.remove_cart,name='remove_cart'),
    path('fav',ev.fav_page,name='fav_page'),
    path('favviewpage',ev.favviewpage,name='favviewpage'),
    path('remove_fav/<str:fid>',ev.remove_fav,name='remove_fav'),



]