from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, About
from django.db.models import Q

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

def blogs(request, slug):
    single_blog=get_object_or_404(Blog,slug=slug, status='Published')
    context={'single_blog':single_blog}
    return render(request, 'BlogPage.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status="Published")
    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)