from cart_test.models import User, Cart, Product, CartItem, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'shipping_address', 'created_on', 'updated_on')


# class TimeStampSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = time_stamp
#         fields = ('created_on', 'updated_on')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'cart_code', 'total_price', 'paid_boolean', 'created_on', 'updated_on')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product 
        fields = ('price', 'name', 'description', 'cart', 'created_on', 'updated_on')

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem 
        fields = ('cart', 'product', 'quantity', 'line_total', 'created_on', 'updated_on')
