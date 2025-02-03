from rest_framework.routers import DefaultRouter
from apps.main.views import ProductMixins

router = DefaultRouter()

router.register(r'products', ProductMixins, basename='product')

urlpatterns = router.urls

