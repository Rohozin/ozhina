from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',views.home, name='home'),
    path('getdressed',views.getdressed, name='getdressed'),
    path('teach',cache_page(60) (views.teach), name='teach'),
    path('product',cache_page(60) (views.product), name='product'),
    path('<slug:category_slug>', views.getdressed, name = 'products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name = 'product_detail'),
    path('<slug:teach_slug>', views.teach, name = 'teach'),
    path('account/login/', views.user_login, name='login'),
    path('edit/', views.edit, name='edit'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('order_create/', views.order_create, name='order_create'),
]