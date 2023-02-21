from django.urls import path
from account.views import UserRegeitrationView,UserLoginView


urlpatterns = [
    path('registration/',UserRegeitrationView.as_view(),name='reg'),
    path('login/',UserLoginView.as_view(),name='login'),
]
