from .serializers import CategorySerializer
from .serializers import CategoryListSerializer
from rest_framework import generics
from .models import Category

# Create your views here.

#@api_view(['GET'])
#def index(request):
#    return Response({"message":"Hello world"})

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset  = Category.objects.all()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()
