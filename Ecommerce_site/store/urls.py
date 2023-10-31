from django.urls import path
from . import views
from store.controler import authviews,carts,wishlist,checkout,order


urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slag>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slag>/<str:prod_slag>',views.productview,name='productview'),
    path('product-list',views.productlistAjex),
    path('searchproduct',views.searchproduct,name='searchproduct'),

    path('register/', authviews.register, name='register'),
    path('login/', authviews.loginpage, name='loginpage'),
    path('logout/', authviews.logoutpage, name='logoutpage'),

    path('add-to-cart/',carts.addtocart,name='addtocart'),
    path('cart',carts.viewcart,name='cart'),
    path('update-cart/',carts.updatecart,name='updatecart'),
    path('delete-cart-item/',carts.deletecartitem,name='deletecartitem'),

    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist/', wishlist.addtowishlist, name='addtowishlist'),
    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),


    path('proceed-to-pay',checkout.razorpaycheck),
    path('my-orders',order.index,name="myorders"),
    path('view-order/<str:t_no>',order.vieworder,name="orderview"),

    
    

]
