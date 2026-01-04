from django.db import models

# Create your models here.
class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.about_title
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform_name