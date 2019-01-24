from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Name')
    email = models.EmailField(max_length=50, blank=False, null=False, verbose_name='Email')


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Title')
    text = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Text')
    user = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    mark = models.ManyToManyField(User, through='Mark', related_name='post', verbose_name='Mark')
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class Mark(models.Model):
    MARKS_CHOICES = (
        ('1', 'Terrible'),
        ('2', 'Bad'),
        ('3', 'Neutral'),
        ('4', 'Good'),
        ('5', 'Perfect')
    )
    mark = models.CharField(max_length=20, choices=MARKS_CHOICES)
    user = models.ForeignKey(User, related_name='marks', on_delete=models.PROTECT, null=True)
    post = models.ForeignKey(Post, related_name='marks', on_delete=models.PROTECT, null=True)


class Comment(models.Model):
    text = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Text')
    user = models.ForeignKey(User, related_name='comments', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

