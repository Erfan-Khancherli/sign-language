from rest_framework import serializers

from .models import Words , Category




        
# class Alphabetserialaizer(serializers.ModelSerializer):
#     class Meta :
#         model = Alphabets
#         fields = '__all__'
        
class Categoryserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id' , 'category_title' , 'image']
        # read_only_fields = ['created_by_id']
class Wordsserializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Words
        fields = ['id' , 'title' , 'image' , 'description' , 'category']
        depth = 1
        ordering = ['title']
        # read_only_fields = ['created_by_id']


        
# class Alphabet_imageserializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Alphabet_image
#         fields = '__all__'
        
        
# class Alphabet_itemserializer(serializers.ModelSerializer):
#     category = Categoryserializer()
#     words = Wordsserializer()
#     alphabet_image = Alphabet_imageserializer()
#     alphabets = Alphabetserialaizer()
#     class Meta:
#         model = Alphabets_item
#         fields = ['id' , 'alphabets','category' ,'words' , 'alphabet_image' ,'alphabet_item_title','time_added','time_last_edited' ]
#         depth = 1
#         ordering = ['id']
        
        
#     def create(self ,  validated_data):
#         word_data = validated_data.pop('words')
#         category_data = validated_data.pop('category')
#         alphabet_image_data = validated_data.pop('alphabet_image')
#         alphabets_data = validated_data.pop('alphabets')
#         alphabets_instance  = Alphabets.objects.create(**alphabets_data)
#         word_instance = Words.objects.create(**word_data)
#         category_instance = Category.objects.create(**category_data)
#         alphabet_image_instance = Alphabet_image.objects.create(**alphabet_image_data)
#         alphabet = Alphabets_item.objects.create(alphabets = alphabets_instance,words=word_instance ,category=category_instance,alphabet_image=alphabet_image_instance , **validated_data)
#         return alphabet
        