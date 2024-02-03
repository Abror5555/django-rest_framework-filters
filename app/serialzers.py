from rest_framework import serializers
from app.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'about']
