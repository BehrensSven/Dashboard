from django.urls import path
from .views import api_overview, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('api/', api_overview),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]