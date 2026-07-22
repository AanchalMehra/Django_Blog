from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','status','isFeatured')
    search_fields=('title','category__category_name','id','status')
    list_editable=('status','isFeatured')

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
