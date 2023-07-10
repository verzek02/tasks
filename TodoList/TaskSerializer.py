from rest_framework import serializers
from TodoList.models import *


class TitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
