from rest_framework import serializers
from bolyuk.models  import Category

class CategorySerializer(serializers.ModelSerializier):
     class Meta:
        model = Category
        fields = ('id', 'name', 'position', 'created', 'updated')