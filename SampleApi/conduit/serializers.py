from rest_framework import serializers
from conduit import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Article
        fields='__all__'
