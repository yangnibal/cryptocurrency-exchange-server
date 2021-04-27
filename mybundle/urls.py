"""mybundle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework import routers, permissions
from account.views import UserViewSet
from card.views import CardViewSet, CryptoViewSet, ExchangeViewSet, CurrencyViewSet, CardGroupViewset
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info( 
        title="Bundle API", 
        default_version="v1", 
        description="Bundle API DOCS", 
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(name="wonjun", email="yangwon.jun.dev@gmail.com"),  
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet), 
router.register(r'cards', CardViewSet),
router.register(r'cryptos', CryptoViewSet)
router.register(r'exchanges', ExchangeViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'card-groups', CardGroupViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
