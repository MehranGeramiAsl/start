from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Category,Product,File
from .serializers import CategorySerializer,ProductSerializer,FileSerializers


class ProductListView(APIView):
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True,context={'request':request})
        return Response(serializer.data)