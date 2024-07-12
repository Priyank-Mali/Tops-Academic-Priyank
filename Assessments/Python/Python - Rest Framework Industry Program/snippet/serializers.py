from rest_framework import serializers
from .models import Snippets

class SnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['title', 'code' , 'linenos' , 'language' , 'style' ]