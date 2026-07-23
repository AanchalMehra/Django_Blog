
from .models import Category,SocialLink


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_links(request):
    links=SocialLink.objects.all()
    return dict(links=links)