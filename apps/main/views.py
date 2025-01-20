from rest_framework.generics import CreateAPIView
from apps.main.models import Settings, Products
from apps.main.serializer import SettingsSerializer, ProductSerializer

class CreateSettingsView(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    
    
class ProductCreateView(CreateAPIView):
    queryset = Products
    serializer_class = ProductSerializer
