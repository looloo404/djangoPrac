from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views

app_name = 'users'

urlpatterns = [
    path('login/',views.login, name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('signupProcess/',views.signupProcess,name='signupProcess'),
    path('logout/',views.logout, name = 'logout'),
    path('loginProcess/',views.loginProcess, name = 'loginProcess')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
