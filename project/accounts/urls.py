from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, UserDetailView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', success_url='webapp:index'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html', next_page='webapp:index'), name='logout'),
    path('create/user/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
]
