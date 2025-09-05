"""
Main URL configuration for BuyItMe application
Imports all sub-URL configurations
"""
from django.urls import path, include

urlpatterns = [
    path('auth/', include('buyitme_app.urls.auth_urls')),
    path('products/', include('buyitme_app.urls.product_urls')),
    path('cart/', include('buyitme_app.urls.cart_urls')),
    path('orders/', include('buyitme_app.urls.order_urls')),
    path('wishlists/', include('buyitme_app.urls.wishlist_urls')),
]