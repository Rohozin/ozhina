from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('getdressed', views.getdressed, name='getdressed'),
    path('teach', views.teach, name='teach'),
    path('product',views.product, name='product'),
    path('addavatar',views.addavatar, name='addavatar'),
    path('<slug:category_slug>', views.getdressed, name = 'products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name = 'product_detail'),
    path('<slug:teach_slug>', views.teach, name = 'teach'),
    path('account/login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done')
]