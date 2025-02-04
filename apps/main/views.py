from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.main.models import Settings, Products
from apps.main.serializer import  ProductSerializer
from apps.main.pagination import ProductPagination

class ProductMixins(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination