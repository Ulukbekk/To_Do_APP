from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('users/', include('users.urls')),
        path('tasks/', include('tasks.urls')),
    ]))]

urlpatterns += docs
