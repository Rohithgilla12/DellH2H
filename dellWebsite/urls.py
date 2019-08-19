"""dellWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from product.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'products/(?P<pk>\d{0,50})/$', productDetailView, name='productDetailView'),
    url(r'expressCheckout/(?P<pk>\d{0,50})/$', checkedOutConfirm, name='expressCheckout'),
    url(r'askBikki/(?P<pk1>\d{0,50})/(?P<pk2>\d{0,50})', askBikki, name= 'askBikkiCompare'),
    url(r'checkout/$', checkOut, name= "checkoutPage"),
    url(r'checkout/compare/$', compareProducts, name= "checkoutPage"),
    url(r'checkout/complete/$', finishCheckout, name= "checkoutComplete"),
    url(r'checkout/shareChat/$', shareChatComponent, name = 'shareChat')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
