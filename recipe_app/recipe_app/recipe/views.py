# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from rest_framework import viewsets
from .models import Category, Recipe
from .serializers import RecipeSerializer

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response


# from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


# @csrf_exempt
@api_view(['GET', 'POST'])
def recipe_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return  Response({'error': 'No data'},status=status.HTTP_404_NOT_FOUND)

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
        return Response(status=status.HTTP_204_NO_CONTENT)
