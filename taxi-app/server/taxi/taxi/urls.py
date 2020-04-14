from django.contrib import admin
from django.urls import path

from trips.views import SignUpView, LogInView, LogOutView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sign_up/', SignUpView.as_view(), name='sign_up'),
    path('api/log_in/', LogInView.as_view(), name='log_in'), # new
    path('api/log_out/', LogOutView.as_view(), name='log_out'), # new
]