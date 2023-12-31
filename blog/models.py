from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ManyToManyField('Category', blank=True)
    post_created = models.DateTimeField(auto_now_add=True)
    post_published = models.DateTimeField(null=True, blank=True)
    post_image = models.ImageField(upload_to='blog_images/%Y/%m/%d/', blank=True)

    STATUS_CHOICES = (
        ('cd', 'canceled'),
        ('pg', 'processing'),
        ('pd', 'posted'),
    )

    post_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='pg')

    def __str__(self):
        return self.title

    def get_author_name(self):
        return str(self.author)

    def get_comments_count(self):
        comments_count = self.comment_set.all().count()
        return comments_count

    def get_post_category(self):
        categories = self.category.all()
        return ', '.join(str(cat) for cat in categories)

    class Meta:
        permissions = [
            ('set_post_status', 'Can set the status of the post to either publish or not'),
        ]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=500)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'Comment №{self.pk}'
