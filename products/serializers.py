from .models import Category,Product,File
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','description','avatar','url']

class FileSerializers(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta :
        model = File
        fields = ['id','title','file','file_type']
    def get_file_type(self,obj):
        return obj.get_file_type_display()
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializers(many=True)
    class Meta :
        model = Product
        fields = ['id','title','description','avatar','categories','files','url']