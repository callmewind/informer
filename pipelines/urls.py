from .views import *
from django.urls import path, include

app_name = 'pipelines'

urlpatterns = [
    path('<slug:environment>/', include([
        path('', PipelineList.as_view(), name='home'),
        path('new/', PipelineCreate.as_view(), name='new'),
        path('<uuid:id>/history/', PipelineHistory.as_view(), name='history'),
        path('<uuid:id>/edit/', PipelineEdit.as_view(), name='edit'),
        path('<uuid:id>/remove/', PipelineRemove.as_view(), name='remove'),
    ]))
]
