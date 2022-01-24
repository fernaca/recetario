from django.urls import path

#Importamos las vistas que mapeamos
from .views import HomeView, ArticleDetailView, PostView, UpdatePostView, DeletePostView

urlpatterns = [
#    path('', views.home, name="home"),
     path('', HomeView.as_view(), name="home"),
     path('article/<int:pk>', ArticleDetailView.as_view(), name="detail"),
     path('add_post/', PostView.as_view(), name="add_post"),
     path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
     path('article/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),

]
