from django.urls import path, include
from rest_framework import routers
from .viewsets import UserViewSet, NewsViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginView 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]