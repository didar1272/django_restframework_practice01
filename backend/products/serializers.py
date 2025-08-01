from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = Product
        fields = ['owner', 'url', 'pk', 'email',
            'title','content','price', 
            'sale_price', 'my_discount']
    
    def get_url(self, obj):
        # return f"/api/products/{obj.id}/"

        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()