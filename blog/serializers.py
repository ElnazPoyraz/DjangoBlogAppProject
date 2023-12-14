from rest_framework import serializers

from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_field = ["id"]


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # read only
    category_id = serializers.IntegerField()

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_field = ["id","created_date", "updated_date"]