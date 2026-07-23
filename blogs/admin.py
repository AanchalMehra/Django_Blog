from django.contrib import admin
from .models import About, Category, Blog, SocialLink

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','status','isFeatured')
    search_fields=('title','category__category_name','id','status')
    list_editable=('status','isFeatured')

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About)
admin.site.register(SocialLink)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=About.objects.all().count()
        if count==0:
            return True
        else :
            return False