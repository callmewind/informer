from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from .api import router
from rest_framework.schemas import get_schema_view
from .views import Home
from configuration.forms import LoginForm

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm)),
    path('', include('django.contrib.auth.urls')),
    path('pipelines/<slug:environment>/', include([
        path('', include('pipelines.urls')),
        path('contacts/', include('contacts.urls')),    
    ])),
    path('config/', include('configuration.urls')),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('auth/', include('rest_framework.urls')),
        path('openapi/', get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'), 
        path('<slug:environment>/', include(router.urls)),
    ])) 
    
]
