from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserListView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/login', include('rest_auth.login.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
