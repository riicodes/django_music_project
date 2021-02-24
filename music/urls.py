from django.urls import path
from . import views
from .views import AlbumList, AlbumDetail, AlbumCreate, AlbumUpdate, AlbumDelete, UserFormView

app_name = 'music'

urlpatterns = [
	path('', AlbumList.as_view(), name='index'),
	path('album/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
	path('album/create/', AlbumCreate.as_view(), name='album-create'),
	path('album/<int:pk>/update/', AlbumUpdate.as_view(), name='album-update'),
	path('album/<int:pk>/delete/', AlbumDelete.as_view(), name='album-delete'),

	path('register/', UserFormView.as_view(), name='register')
]