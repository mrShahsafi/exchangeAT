from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Token obtain (login) endpoint
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # Token refresh endpoint
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
