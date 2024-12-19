from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, CustomLoginView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', CustomLoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]