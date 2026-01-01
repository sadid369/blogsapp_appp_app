from blogs.models import Blog, Category
from django.contrib.auth.models import User
import re
from django.utils.text import slugify
# how to run:  python manage.py shell < blogsapp/load_blogs.py
#  python manage.py shell < load_blogs.py
# usernames = [
#     "john_doe", "mia_traveler", "chef_ava", "dev_raj", "dr_lisa", "eco_emma"
# ]
# for username in usernames:
#     user, created = User.objects.get_or_create(username=username, defaults={"password": "pbkdf2_sha256$260000$dummy$dummy"})
#     if created:
#         print(f"Created user: {username}")

def get_category(name):
    return Category.objects.get_or_create(category_name=name)[0]

def get_user(username):
    return User.objects.get(username=username)

def get_unique_slug(title):
    base_slug = slugify(title)
    slug = base_slug
    counter = 1
    while Blog.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


blogs_data = [
    {
        "title": "The Future of Artificial Intelligence in 2026",
        "category": "Technology",
        "author": "john_doe",
        "featured_image": "uploads/2025/12/27/ai.jpg",  # You need to upload the image or leave blank/null
        "short_description": "Exploring how AI will transform industries like healthcare, education, and transportation in the coming year.",
        "blog_body": "AI advancements in 2026 include multimodal models, ethical guardrails, and edge AI deployment...",
        "status": "Published",
        "is_featured": True,
    },
    {
        "title": "Top 10 Hidden Beaches in Southeast Asia",
        "category": "Travel",
        "author": "mia_traveler",
        "featured_image": "uploads/2025/12/27/beach.jpg",
        "short_description": "Discover pristine, lesser-known beaches away from the tourist crowds.",
        "blog_body": "From Thailand’s Koh Lipe to Indonesia’s Raja Ampat...",
        "status": "Published",
        "is_featured": False,
    },
    {
        "title": "Vegan Baking 101: Easy Desserts Without Dairy or Eggs",
        "category": "Food",
        "author": "chef_ava",
        "featured_image": "uploads/2025/12/27/vegan.jpg",
        "short_description": "Learn how to make delicious vegan desserts using simple pantry staples.",
        "blog_body": "Flax eggs, aquafaba, and banana substitutes...",
        "status": "Published",
        "is_featured": True,
    },
    {
        "title": "Understanding Django ORM for Beginners",
        "category": "Technology",
        "author": "dev_raj",
        "featured_image": "uploads/2025/12/27/django.jpg",
        "short_description": "A beginner-friendly guide to using Django's powerful ORM.",
        "blog_body": "How to create models, run queries, and avoid N+1...",
        "status": "Draft",
        "is_featured": False,
    },
    {
        "title": "Winter Wellness: Staying Healthy During the Holidays",
        "category": "Health",
        "author": "dr_lisa",
        "featured_image": "uploads/2025/12/27/wellness.jpg",
        "short_description": "Tips to boost immunity and manage holiday stress.",
        "blog_body": "Sleep hygiene, vitamin D, mindful eating...",
        "status": "Published",
        "is_featured": False,
    },
    {
        "title": "Sustainable Fashion: Brands That Care About the Planet",
        "category": "Lifestyle",
        "author": "eco_emma",
        "featured_image": "uploads/2025/12/27/fashion.jpg",
        "short_description": "Ethical and eco-friendly fashion brands making a difference in 2025.",
        "blog_body": "Circular fashion, recycled materials, transparency reports...",
        "status": "Published",
        "is_featured": True,
    },
    {
        "title": "How to Start a Personal Blog in One Weekend",
        "category": "Technology",
        "author": "john_doe",
        "featured_image": "uploads/2025/12/27/blog.jpg",
        "short_description": "Step-by-step guide to launching your blog using Django.",
        "blog_body": "Project setup, deployment, custom domains...",
        "status": "Draft",
        "is_featured": False,
    },
]

# Set the username for all blogs
all_blogs_author = "sadid"
author_user = get_user(all_blogs_author)

for data in blogs_data:
    blog = Blog.objects.create(
        title=data["title"],
        slug=get_unique_slug(data["title"]),
        category=get_category(data["category"]),
        author=author_user,  # Use the same user for all blogs
        short_description=data["short_description"],
        blog_body=data["blog_body"],
        status=data["status"],
        is_featured=data["is_featured"],
        # featured_image can be set if you upload images via Django admin or handle file uploads
    )
    print(f"Created: {blog.title}")