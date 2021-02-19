
from django.urls import path
from .views import HomeView, DetailsView, AddPostView, EditPostView, DeletePostView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', DetailsView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit_post/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('delete/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
