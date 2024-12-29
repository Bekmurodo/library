from django.urls import path
from .views import (
    BookListApi,
    book_list_view,
    BookDetailApiView,
    BookDeleteApiView,
    BookUpdateApiView,

 )

urlpatterns = [
    path('', BookListApi.as_view(),),
    path('<int:pk>/', BookDetailApiView.as_view()),
    path('<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('<int:pk>/update/', BookUpdateApiView.as_view()),
    path('books/', book_list_view)
]
