from django.shortcuts import render
from .serializers import CategorySerializers, DocumentSerializers
from .models import Categories, Documents
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ListCategoryAPIView(APIView):
    def get(self, request):
        category = Categories.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class DocumentListAPIView(APIView):
    def get(self, request):
        documents = Documents.objects.all()
        serializer = DocumentSerializers(documents, many=True)
        serializer_data = {
            'Category id': [i['category_name'] for i in serializer.data],
            'Name': [j['name'] for j in serializer.data]
        }
        return Response(serializer_data)


class DocumentsAPIView(APIView):
    def get(self, request, pk):
        documents = Documents.objects.get(pk=pk)
        serializer = DocumentSerializers(documents)
        return Response(serializer.data)