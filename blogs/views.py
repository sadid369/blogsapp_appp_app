from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Blog, Category

# Create your views here.
def post_by_category(request, category_id):
    posts = Blog.objects.filter(category__id=category_id, status="Published")
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    # try:
    #     category = Category.objects.get(id=category_id)
    # except Category.DoesNotExist:
    #     return redirect('home')
    context = {
        "posts": posts,
        "categories": categories,
        "category": category,
    }
    return render(request, "posts_by_category.html", context)
