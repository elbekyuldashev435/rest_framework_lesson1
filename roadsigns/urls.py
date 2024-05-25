from django.urls import path
from .views import ListCategoryAPIView, DocumentListAPIView, DocumentsAPIView


urlpatterns = [
    path('category-list/', ListCategoryAPIView.as_view(), name='category-list'),
    path('document-list/', DocumentListAPIView.as_view(), name='document-list'),
    path('category-list/detail/<int:pk>/', DocumentsAPIView.as_view(), name='detail')
]