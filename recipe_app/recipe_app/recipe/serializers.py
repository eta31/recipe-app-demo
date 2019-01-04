from rest_framework import serializers
from .models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta(object):
        """docstring for Meta"""
        model = Category
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta(object):
        """docstring for Meta"""
        model = Recipe
        fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):

#      # class Meta:
#      #    model = Category
#      #    fields = '__all__'

#     id = serializers.IntegerField(read_only=True)
#     category_name = serializers.CharField(required=True, allow_blank=False, max_length=100)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Category.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.category_name = validated_data.get('category_name', instance.category_name)
#         instance.save()
#         return instance

# class RecipeSerializer(serializers.ModelSerializer):

#     id = serializers.IntegerField(read_only=True)
#     recipe_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     ingredients = serializers.CharField(required=True, allow_blank=False, max_length=255)
#     instructions = serializers.CharField(required=True, allow_blank=False)
#     serving_size = serializers.IntegerField(required=True)
#     category = serializers.IntegerField(required=True)
#     # category_name = serializers.RelatedField(source='category', read_only=True)
#     notes = serializers.CharField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Recipe.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.recipe_name = validated_data.get('recipe_name', instance.recipe_name)
#         instance.ingredients = validated_data.get('ingredients', instance.ingredients)
#         instance.instructions = validated_data.get('instructions', instance.instructions)
#         instance.serving_size = validated_data.get('serving_size', instance.serving_size)
#         instance.category = validated_data.get('category', instance.category)
#         instance.notes = validated_data.get('notes', instance.notes)
#         instance.save()
#         return instance
