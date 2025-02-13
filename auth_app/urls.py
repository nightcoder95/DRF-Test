from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserView, GetUsers

urlpatterns = [
    # Registration endpoint:
    path('register/', RegisterView.as_view(), name='register'),
    # JWT endpoints:
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserView.as_view(), name='user_profile'),
    path('getUsers/', GetUsers.as_view(), name='get_users'),
]