
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('token-auth', obtain_jwt_token),
    # path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api/', include('articles.api.urls')),
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    ]