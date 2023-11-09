from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    # owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Product
        fields = '__all__'


