from .models import Category,Product,File
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','description','avatar']

class FileSerializers(serializers.ModelSerializer):
    class Meta :
        model = File
        fields = ['title','file']
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializers(many=True)
    class Meta :
        model = Product
        fields = ['id','title','description','avatar','categories','files','url']