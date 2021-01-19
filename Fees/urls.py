from django.urls import path,include
from .views import *


urlpatterns = [
    path('',add_Fees,name='add_Fees'),
    path('register',register,name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup',signup)
]
