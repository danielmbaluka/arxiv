from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import RegistrationView

urlpatterns = [
    url(r"^token/$", TokenObtainPairView.as_view(), name="token_login"),
    url(r"^token/refresh/$", TokenRefreshView.as_view()),
    url(r"^signup/$", RegistrationView.as_view()),
]
