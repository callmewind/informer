from .views import *
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('environments/', include([
        path('', EnvironmentList.as_view(), name='environment_list'),
        path('create/', EnvironmentCreate.as_view(), name='environment_create'),
        path('<slug:slug>/remove/', EnvironmentRemove.as_view(), name='environment_remove'),
    ])),
    path('channels/', include([
        path('', ChannelList.as_view(), name='channel_list'),
        path('<slug:type>/create/', ChannelCreate.as_view(), name='channel_create'),
        path('<int:pk>/update/', ChannelUpdate.as_view(), name='channel_update'),
        path('<int:pk>/remove/', ChannelRemove.as_view(), name='channel_remove'),
    ])),
]
