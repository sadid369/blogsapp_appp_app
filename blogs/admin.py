from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category','is_featured', 'status')
    search_fields= ('id','title','status', 'category__category_name','author__username')
    list_editable = ('is_featured', 'status')
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)