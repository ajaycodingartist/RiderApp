from django.urls import path, include
from . import views
from app1.views import index
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RideViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rides', RideViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]