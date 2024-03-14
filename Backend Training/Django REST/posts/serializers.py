from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created"]  # fields = "__all__"
        read_only_fields = ["id", "created"]
        # exclude = ["roll"]

    def validate_title(self, value):
        if value == "ok":
            raise serializers.ValidationError("Title should not be ok")
        return value

    # Object Level
    def validate(self, data):
        title = data.get("title")
        content = data.get("content")
        if title and content:
            if len(title) < 2 or len(content) < 2:
                raise serializers.ValidationError("Object Level Validation")
        return data
