# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# from rest_framework import viewsets
from .models import Category, Recipe
from .serializers import RecipeSerializer,CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



@csrf_exempt
@api_view(['GET', 'POST'])
def recipe_list(request):
    """
    List all recipes, or create a new recipe.

    get:
        List all recipes

    post:
        Create new recipe

        Example POST request

        Do not forget create category before creating recipe!

        {
            "recipe_name": "Ricotta Meatballs",
            "ingredients": "onion, olive oil, garlic, ground beef, cheese, egg",
            "instructions": "Saute onion in 2 tablespoons olive oil in a skillet over medium heat until onion is translucent, about 5 minutes. Stir garlic into onion and turn off heat. Transfer onion mixture to a large mixing bowl.Stir ground beef, ricotta cheese, parsley, egg, kosher salt, black pepper, and cayenne pepper with onion mixture until almost combined; stir in bread crumbs and continue to mix until thoroughly blended",
            "serving_size": 2,
            "category": 3,
            "notes": "Aluminum foil can be used to keep food moist, cook it evenly, and make clean-up easier."
        }
    """
    if request.method == 'GET':

        recipes = Recipe.objects.all()

        if len(recipes) == 0:
            return  Response({'message': 'No data for this criteria'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    """
    Retrieve, update or delete for recipe.

    get:
        Get specific recipe by recipe id

    put:
        Update recipe details by recipe id

        Example PUT request

        {
            "recipe_name": "Ricotta Meatballs",
            "ingredients": "onion, olive oil, garlic, ground beef, cheese, egg",
            "instructions": "Saute onion in 2 tablespoons olive oil in a skillet over medium heat until onion is translucent, about 5 minutes. Stir garlic into onion and turn off heat. Transfer onion mixture to a large mixing bowl.Stir ground beef, ricotta cheese, parsley, egg, kosher salt, black pepper, and cayenne pepper with onion mixture until almost combined; stir in bread crumbs and continue to mix until thoroughly blended",
            "serving_size": 3,
            "category": 4,
            "notes": "Aluminum foil can be used to keep food moist, cook it evenly, and make clean-up easier."
        }
    delete:
        Delete recipe by recipe id
    """
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return  Response({'error': 'No data for this criteria'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recipe.delete()
        return Response({'success': 'Recipe deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
@api_view(['GET', 'POST'])
# @permission_classes((AllowAny,))
def category_list(request):
    """
    List all categories for recipe, or create a new category.

    get:
        Get all categories of recipes

    post:
        Create new category

        Example POST request

        {
            "category_name":"Main Dishes"
        }

    """
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
