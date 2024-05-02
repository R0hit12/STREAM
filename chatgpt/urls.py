from django.urls import path
from .views import *

urlpatterns = [
    path('stream/', stream_completions, name='stream_view'),
    # path('api/', stream_completions)
    # path('query_view/',query_view, name = 'query_view')
]
