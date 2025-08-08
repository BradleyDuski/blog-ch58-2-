from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post

# Create your views here.
#PostsListView is going to retrieve all the objects from the post table in the db

class PostListView(ListView):
    #template_name attributes is going to be to render a specific html file
    template_name="posts/list.html"
    #model is going to be from which table we want to retrieve the data
    model=Post
    #context is a python dictionary that holds the data for the generic views
    #and this context travels to the htmls
    #by default the context name of Listview and DetailView is "object" or "object_lists"
    #context_object_name would allow us to modifyy that name and how to call it in the htmls
    context_object_name="posts"

#PostDetailView is going to retrieve a single element from the post table in the db



class PostDetailView(DetailView):
    template_name="posts/detail.html"
    model=Post
    context_object_name="single_post"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model=Post
    fields=["title", "subtitle", "body"]