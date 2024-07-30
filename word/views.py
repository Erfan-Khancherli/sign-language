from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from word.models import Alphabets_item , Category
from word.serializers import Alphabet_itemserializer ,Categoryserializer
from rest_framework import status
from rest_framework.response import Response
import json 


# Create your views here.
class AlphabetListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Alphabet_itemserializer
    queryset = Alphabets_item.objects.all()
    
    
class AlphabetCreate(APIView):
    permission_classes = (AllowAny,)
    serializer_classes = Alphabet_itemserializer
    
    def get_object(self, pk):
        try:
            return Alphabets_item.objects.get(pk=pk)
        except Alphabets_item.DoesNotExist:
            raise Http404
    def post(self , request):
        
        serializer = Alphabet_itemserializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Categoryserializer
    queryset = Category.objects.all()
    
class get_1_alphabet(APIView):
    permission_classes = (AllowAny,)
    def get(self , request):
        qs = request.data.dict()
        print(qs['alphabets.title'])
        queryset = Alphabets_item.objects.all().filter(alphabets__title=qs['alphabets.title'])
        serializer   = Alphabet_itemserializer(queryset,many=True )
        print('**************')
        print(serializer.data)
        return Response(serializer.data)
        