from django.contrib import admin
from django.urls import path
from . import views
# from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                # #   path('', HomePageView.as_view(), name='home'),
                  path('index/', views.index,name="index"),
                  path('footer/', views.footer,name='footer'),
                  path('orderplace/', views.orderplace,name='orderplace'),
                  path('checkout_cart/', views.checkout_cart,name='checkout_cart'),
                  path('cart_item/', views.show_cart,name='show_cart'),
                  path('increase_quantity/<int:product_id>/', views.increase_cart_quantity, name='increase_quantity'),
                  path('decrease_quantity/<int:product_id>/', views.decrease_cart_quantity, name='decrease_quantity'),
                  path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
                  path('checkout_complete/', views.checkout_complete,name='checkout_complete'),
                  path('checkout_info/', views.checkout_info,name='checkout_info'),
                  path('checkout_payment/', views.checkout_payment,name='checkout_payment'),
                  path('contact_us/', views.contact_uss,name='contact_us'),
                  path('faq/', views.faq,name='faq'),
                  path('index_fixed_header/', views.index_fixed_header,name='index_fixed_header'),
                  path('index_inverse_header/', views.index_inverse_header,name='index_inverse_header'),
                  path('my_account/', views.my_account,name='my_account'),
                  path('product_detail/<int:id>', views.product_detail,name='product_detail'),
                  path('product/', views.product,name='product'),
                  path('about_us', views.about_us,name='about_us'),
                  path('search_results/', views.search_results,name='search_results'),
                  path('sign_in/',views.sign_in,name='sign_in'),
                  path('login/',views.log_in,name='login'),

                # #   # Cart urls
                  # path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
                  # path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
                  # path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
                  # path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
                  # path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
                  # path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
                  
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)