from django.urls import path
from authentication.views import *

urlpatterns = [
    path('signup/user/', signUpUser),
    path('signup/manager/', signUpManager),
    path('signup/merchant/', signUpMerchant),
    path('signin/', signIn),
    path('confirm/', confirmUser)
]
