from django.urls import path
from apps.main.views import CreateSettingsView, ProductCreateView

urlpatterns = [
    path("settings/create/", CreateSettingsView.as_view(), name="settings_create"),
    path('product/create', ProductCreateView.as_view(), name="product_create")
]
