from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Favorite
from rest_framework import status
from rest_framework.response import Response
from .serializers import FavoriteSerializer
from word.models import Words

class FavoriteListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

class FavoriteCreate(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteSerializer 
    def post(self, request, word_id):
        user = request.user 
        try:
            word = Words.objects.get(id=word_id)
        except Words.DoesNotExist:
            return Response({'error': 'Word not found'}, status=status.HTTP_404_NOT_FOUND)
        favorite = Favorite.objects.filter(user=user, word=word).first()
        if favorite:
            favorite.delete()
            return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
        else:
            f_id = Favorite.objects.create(user=user, word=word ,created_by=self.request.user)
            word.favorite = f_id  
            word.save()
            return Response({'message': 'Liked'}, status=status.HTTP_201_CREATED)