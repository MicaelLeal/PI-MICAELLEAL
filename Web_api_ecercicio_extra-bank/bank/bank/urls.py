from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', views.account_list),
    path('accounts/<int:account_id>/', views.account_detail),
]
