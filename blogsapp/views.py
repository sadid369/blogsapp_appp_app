from django.shortcuts import render,redirect
from blogs.models import Blog, Category
from about.models import About

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False ,status="Published").order_by('-created_at')
    about = About.objects.get()
    context = {
        "categories": categories,
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
    }
    return render(request, "home.html", context)