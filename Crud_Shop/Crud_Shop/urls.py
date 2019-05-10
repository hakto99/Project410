from django.conf.urls import url, include
from django.contrib import admin

from .views import home

from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('accounts.urls', namespace='accounts')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^Crud_Shop/', include('shopping_cart.urls', namespace='shopping_cart')),
    url(r'^home', home),
    url(r'^accounts/login', login_view),
    url(r'^accounts/register', register_view),
    url(r'^accounts/logout', logout_view)

]
