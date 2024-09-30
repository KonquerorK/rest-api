from django.urls import include, path
from .views import RegisterView, ResetPasswordView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', TokenObtainPairView.as_view(), name='login'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
   path('profile/', UserProfileView.as_view(), name='user_profile'),
]
