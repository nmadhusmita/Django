from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user_account.urls")),
    path('user_account/', include('django.contrib.auth.urls'))
]