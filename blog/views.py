from django.shortcuts import render
from django.views import View
from .forms import PostcreateForm

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
            
        }
        return render(request,'blog_list.html', context)
    
class BlogCreateView(View):
    def get(self, request, *args, **kargrs):
        context={
        }
        return render(request, 'blog_create.html')

    def get(self, request, *args, **kargrs):
        context={
        }
        return render(request, 'blog_create.html')
    