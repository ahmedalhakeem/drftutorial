from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'owner']
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many = True, queryset= Snippet.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)

#     def create(self, validated_data):

#         return Snippet.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         return super().update(instance, validated_data)