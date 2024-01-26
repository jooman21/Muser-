from django.urls import path

from . import views 
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

   path('api/', views.getRoutes, name='get_routes'),
   path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path( 'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
  
]