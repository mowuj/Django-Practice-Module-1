from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.SignupView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('add_musician/', views.AddMusicianView.as_view(), name='add_musician'),
    path('edit_musician/<int:id>', views.EditMusicianView.as_view(), name='edit_musician'),
    path('delete_musician/<int:id>', views.DeleteMusicianView.as_view(), name='delete_musician'),
]