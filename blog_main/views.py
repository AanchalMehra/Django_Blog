from django.shortcuts import render

from blogs.models import About, Category, Blog

def home(request):
  
    featured_posts=Blog.objects.filter(isFeatured=True, status='Published').order_by('-updated_at')
    Not_featured_posts=Blog.objects.filter(isFeatured=False, status='Published').order_by('-updated_at')
    try:
        about=About.objects.first()
    except About.DoesNotExist:
        about=None
    context={
        'about':about,
        'featured_posts':featured_posts,
        'not_featured_posts':Not_featured_posts
    }
    return render(request,'home.html',context)