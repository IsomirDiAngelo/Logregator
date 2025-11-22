from django.urls import path

from .views import api_token_view, log_view



urlpatterns = [
    path('token/', api_token_view.get),
    path('log/', log_view.get),
    path('log/add', log_view.post)
]