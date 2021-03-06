from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    name = models.CharField('Author Name', max_length=120)
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Its for meta data '-' define descending order, by doing this post published recently will appear first
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
