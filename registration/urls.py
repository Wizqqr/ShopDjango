from django.urls import path
from . import views
from telephone import views as tel_views
app_name = 'registration'
urlpatterns = [
    path('workregister/', views.RegisterView.as_view(), name='registration'),
    path('workerslogin/', views.WorkRegisterView.as_view(), name='workerslogin'),
    path('workerslogout/', views.AuthLogoutView.as_view(), name='workerslogout'),
    path('workerslist/', views.WorkersListView.as_view(), name='workerslist'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('phone_list/', tel_views.PhoneListView.as_view(), name='phone_list'),
]