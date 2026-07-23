from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, pk):
    posts=Blog.objects.filter(category=pk, status='Published').order_by('-created_at')
    category=get_object_or_404(Category, pk=pk)
    '''try:
        category=Category.objects.get(pk=pk)
    except:
        return redirect('home')'''
    context={'posts':posts,'category':category}
    return render(request, 'post_by_category.html', context)