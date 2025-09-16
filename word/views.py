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
from django.forms.models import model_to_dict

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
        category_title = data.get('category[category_title]')
        qs = Category.objects.get(category_title=category_title)
        word_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'image': request.FILES.get('image'),
            'category': qs.id
        }
        word_serializer = Wordsserializer(data=word_data)
        word_serializer.is_valid(raise_exception=True)
        word_serializer.save(created_by=self.request.user)

        return Response(word_serializer.data, status=201)
    
class CategoryList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Categoryserializer
    queryset = Category.objects.all()
    
class CategoryCreate(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    def post(self , request):
        data = request.data.copy()
        serializer = Categoryserializer(data = data)
        if serializer.is_valid(raise_exception = True):
            category = serializer.save(created_by = self.request.user)          
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
