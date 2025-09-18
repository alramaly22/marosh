from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts import views
from orders import views as order_views

urlpatterns = [
    path('', views.index, name='index'),
    path('appetizers/', views.appetizers, name='appetizers'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('kaak/', views.kaak, name='kaak'),
    path('manakish/', views.manakish, name='manakish'),
    path('menu/', views.menu, name='menu'),
    path('pidetr/', views.pidetr, name='pidetr'),
    path('pizza/', views.pizza, name='pizza'),

    # Admin
    path('admin/', admin.site.urls),

    # API الأوردر
    path('api/create-order/', order_views.create_order, name='create_order'),
    path('webhook/stripe/', order_views.stripe_webhook, name='stripe_webhook'),

    # صفحات الدفع
    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),  # ✦ صفحة إلغاء الدفع
    path("checkout/", views.checkout, name="checkout"),  # ✦ صفحة الكارت/الدفع
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
