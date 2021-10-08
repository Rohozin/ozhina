from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getdressed', views.getdressed, name='getdressed'),
    path('teach', views.teach, name='teach'),
    path('product',views.product, name='product'),
    path('addavatar',views.addavatar, name='addavatar'),
    path('<slug:category_slug>', views.getdressed, name = 'products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name = 'product_detail'),
    path('<slug:teach_slug>', views.teach, name = 'teach'),
    path('account/create/', views.signUpView, name='signup'),
    path('account/login/',views.loginView, name='login'),
    path('account/signout/', views.signoutView, name='signout'),
]