from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from conduit import models
from conduit import serializers
# Create your views here.

class CreateArticle(APIView):
    def get(self,request,pk=None,format=None):
        if pk:
            var = models.Article.objects.filter(pk=pk)
        else:
            var = models.Article.objects.all()
            
        serializer = serializers.ArticleSerializer(var,many=True)
        return Response(serializer.data)

class CreateArticleView(generics.ListCreateAPIView):
    serializer_class = serializers.ArticleSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.Article.objects.filter(pk=pk)

class CrudView(generics.RetrieveUpdateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
