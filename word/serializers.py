from rest_framework import serializers
from .models import Words , Category


        
class Categoryserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id' , 'category_title' , 'image']
        write_only_fields = ['image']
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")
        return value
class Categorypackageserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id' , 'category_title']


class Wordsserializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Words
        fields = ['id' , 'title' , 'image' , 'description' , 'category' , 'favorite']
        depth = 1
        ordering = ['title']
        read_only_fields = ['category[image]']
        
        