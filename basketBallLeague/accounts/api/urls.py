from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from accounts.api.views import logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout')
]
