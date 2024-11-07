from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.cus_login,name="login"),
    path('logout',views.cus_logout,name="logout"),
    path('products',views.products,name="products"),
    path('product_detail/',views.shop_detail,name="product_detail"),
    path('contact',views.contact,name="contact"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('testimonial',views.testimonial,name="testimonial"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
