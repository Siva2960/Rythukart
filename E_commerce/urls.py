from django.contrib import admin
from django.urls import path
from Rythukart import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from Rythukart.views import add_to_cart_ajax
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('homee/index.html',views.index),
    path('Login/logout_view/', views.logout_view, name='logout_view'),
    path('',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('homee/', views.home1, name='homee'),
    path('index/', views.index, name='index'),
    path('',views.Register,name='Register'),
    path('Register/', views.Register_view, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('Login/index.html',views.index),
    path('veg/', views.veg, name='veg'),
    path('pappu/', views.pappu, name='pappu'),
    path('rice/', views.rice, name='rice'),
    path('admin_upload/', views.admin_upload, name='admin_upload'),
    path('cart/add_address.html', views.add_address, name='add-address'),
    path('add-address.html', views.add_address, name='add-address'),
    path('', views.location_page, name='location_page'),
    path('save-location/', views.save_location, name='save_location'),
    path('select-address/<int:address_id>/', views.select_address, name='select_address'),
    path('cart/payment.html',views.payment),
    path('cart/', views.cart_view, name='view_cart'),
    path('increase/<int:item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('decrease/<int:item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('add-address/', views.add_address, name='add_address'),
    path('select-address/<int:address_id>/', views.select_address, name='select_address'),
    path('payment/', views.payment, name='payment'),
    path("add_to_cart_ajax/", add_to_cart_ajax, name="add_to_cart_ajax"),
    path('ajax/change-cart/', views.change_cart_quantity_ajax, name='change_cart_ajax'),
    path('remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('orders/', views.order_history, name='order_history'),
    path('invoice/<int:order_id>/', views.generate_invoice, name='generate_invoice'),
    path('voice-add-to-cart/', views.voice_add_to_cart, name='voice_add_to_cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# REMOVE or COMMENT OUT this line:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)