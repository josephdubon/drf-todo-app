from rest_framework import serializers
from todo_app.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )

        model = Todo
