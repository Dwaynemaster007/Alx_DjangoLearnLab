from django.urls import path

from .views import (
    BookDetailUpdateDeleteView,
    BookListCreateView,
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

urlpatterns = [
    # REST-style endpoints
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),
    # One generic view per action
    path('books/list/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/detail/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]
