from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Home / ListView
class HomeView(ListView):
    queryset = Post.objects.order_by('-created_on') #Negativo para el Sort
# Otra form de ordenar: ordering = ['-created_on']
    model = Post
    template_name = 'home.html' 
    
# DetailView
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html' 
    
# CreateView. Pasamos el formulario
class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html' 
    #fields = '__all__'    #  o se le especifica los que se quiere: fields = ('title','body')
    # Como le pasamos el form_class, va a usar todos

# Editar
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html' 
    
# Borrar
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')  #Para el borrado es necesario