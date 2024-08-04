from rest_framework import serializers
from .models import globalNote

class GlobalNoteSeralizer(serializers.ModelSerializer):
    class Meta:
        model = globalNote
        fields = ['student_id' , 'comment']