from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from word.models import Words , Category
from word.serializers import Wordsserializer , Categoryserializer
from rest_framework import status
from rest_framework.response import Response
import json 
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class WordsListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Wordsserializer
    queryset = Words.objects.all()
    
    
class WordsCreate(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_classes = Wordsserializer
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        try:
            return Words.objects.get(pk=pk)
        except Words.DoesNotExist:
            raise Http404
    def post(self , request):
        data = request.data.copy()

        # Extract and create category manually
        category_data = {
            'category_title': data.get('category[category_title]'),
            'image': request.FILES.get('category[image]')
        }
        category_serializer = Categoryserializer(data=category_data)
        category_serializer.is_valid(raise_exception=True)
        category = category_serializer.save(created_by=self.request.user)
        print("*************************")
        print(category.id)
        # Prepare word data with category id
        word_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'image': request.FILES.get('image'),
            'category': category.id
        }
        word_serializer = Wordsserializer(data=word_data)
        word_serializer.is_valid(raise_exception=True)
        word_serializer.save(created_by=self.request.user)

        return Response(word_serializer.data, status=201)
        # data = request.data.copy()

        # category_data = {
        #     'category_title': data.get('category[category_title]'),
        #     'image': data.get('category[image]')
        # }

        # word_data = {
        #     'title': data.get('title'),
        #     'description': data.get('description'),
        #     'category': category_data   
        # }
        # serializer = Wordsserializer(data=word_data)
        # if serializer.is_valid():
        #     # Create Category First
        #     category_instance = Category.objects.create(
        #         category_title=category_data['category_title'],
        #         image=category_data['image']
        #     )

        #     # Create Word with related Category
        #     word_instance = Word.objects.create(
        #         title=word_data['title'],
        #         description=word_data['description'],
        #         category=category_instance
        #     )

        #     return Response({
        #         'word': WordSerializer(word_instance).data
        #     }, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Categoryserializer
    queryset = Category.objects.all()
    
# class get_1_alphabet(APIView):
#     permission_classes = (AllowAny,)
#     def get(self , request):
#         qs = request.data.dict()
#         print(qs['alphabets.title'])
#         queryset = Alphabets_item.objects.all().filter(alphabets__title=qs['alphabets.title'])
#         serializer   = Alphabet_itemserializer(queryset,many=True )
#         print('**************')
#         print(serializer.data)
#         return Response(serializer.data)
        