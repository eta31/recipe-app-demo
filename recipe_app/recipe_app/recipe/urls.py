from django.urls import path
from .views import recipe_list,recipe_detail,category_list

urlpatterns = [
    path('api/recipes/', recipe_list),
    path('api/categories/', category_list),
    path('api/recipes/<int:pk>/', recipe_detail),
]
